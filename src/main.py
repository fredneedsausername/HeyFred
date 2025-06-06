from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os
from fredcrash import enable_crash_logging
from dotenv import load_dotenv
from pathlib import Path
from gevent import monkey   # Leave these two statements at the start else undefined behaviour
monkey.patch_all()          # Leave these two statements at the start else undefined behaviour


# Load environment variables into the program
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


# Decide app flow based on FLASK_ENV
match os.getenv('FLASK_ENV'):
    case 'production':
        app_debug_mode = False
        flask_static_folder = None
    case 'development':
        app_debug_mode = True
        flask_static_folder = str(Path(__file__).resolve().parent.parent / "static")


# Initialize web app
flask_template_folder = str(Path(__file__).resolve().parent.parent / "templates")


app = Flask(__name__, template_folder=flask_template_folder, static_folder=flask_static_folder)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


socketio = SocketIO(app, async_mode='gevent')


from openai import OpenAI
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


@app.route('/')
def index():
    return render_template('chat.html')


@socketio.on('connect')
def on_connect():
    pass


@socketio.on('disconnect')
def on_disconnect():
    pass


@socketio.on('message')
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

    socketio.run(app, debug=app_debug_mode, host='127.0.0.1', port=int(os.getenv('PORT')))