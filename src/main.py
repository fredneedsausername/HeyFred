from flask import Flask, render_template, session, redirect, url_for, request, make_response
from flask_socketio import SocketIO, emit
import os
from fredcrash import enable_crash_logging
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
from functools import wraps
from gevent import monkey   # Leave these two statements at the start else undefined behaviour
monkey.patch_all()          # Leave these two statements at the start else undefined behaviour


# Load environment variables into the program
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


# Initialize web app
flask_template_folder = str(Path(__file__).resolve().parent.parent / "templates")


app = Flask(__name__, template_folder=flask_template_folder)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


socketio = SocketIO(app, async_mode="gevent")


def generate_llm_response(message):    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    try:
        stream = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[{"role": "user", "content": message}],
            stream=True,
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
                
    except Exception as e:
        yield f"Errore durante la generazione: {e}"


def authentication_needed(fn):
    @wraps(fn)
    def implementation(*args, **kwargs):
        if 'user' in session:
            return fn(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return implementation


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == os.getenv('LOGIN_PASSWORD'):
            session['user'] = 'fred'
            response = make_response()
            response.headers['HX-Redirect'] = url_for('index')
            return response
        else:
            return '<div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert"><strong class="font-bold">Errore:</strong><span class="block sm:inline"> Password errata. Riprova.</span></div>'
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/')
@authentication_needed
def index():
    return render_template('chat.html')


@socketio.on('connect')
@authentication_needed
def on_connect():
    pass


@socketio.on('disconnect')
@authentication_needed
def on_disconnect():
    pass


@socketio.on('message')
@authentication_needed
def handle_message(data):
    user_message = data['message']
    
    # Start streaming response
    emit('response_start')
    
    try:
        # Generate and stream LLM response
        for chunk in generate_llm_response(user_message):
            emit('response_chunk', {'chunk': chunk})
            socketio.sleep(0) # Let socketio manage other connections/events
        
        emit('response_complete')
        
    except Exception as e:
        emit('response_error', {'error': f'{e}'})


if __name__ == '__main__':
    # Enable crash logging for both prod and dev
    enable_crash_logging('..')

    # Determine if debug mode based on FLASK_ENV
    app_debug_mode = False if os.getenv('FLASK_ENV') == 'production' else True

    # Run the application with gevent
    socketio.run(app, debug=app_debug_mode, host='127.0.0.1', port=int(os.getenv('PORT')))