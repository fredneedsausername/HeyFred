from flask import Flask, render_template, session, redirect, url_for, request, make_response
from flask_socketio import SocketIO, emit
import os
try:
    from .fredcrash import enable_crash_logging
except ImportError:
    from fredcrash import enable_crash_logging
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
from functools import wraps
from datetime import timedelta
from gevent import monkey   # Leave these two lines at the end of the imports else undefined behaviour
monkey.patch_all()          # Leave these two lines at the end of the imports else undefined behaviour


# Load environment variables into the program
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

cors_origins_str = os.getenv('CORS_ALLOWED_ORIGINS')
allowed_origins = [origin.strip() for origin in cors_origins_str.split(',') if origin.strip()]


# Initialize web app
flask_template_folder = str(Path(__file__).resolve().parent.parent / "templates")


app = Flask(__name__, template_folder=flask_template_folder)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# Time for session to expire
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=31)


socketio = SocketIO(app, async_mode="gevent", cors_allowed_origins=allowed_origins)


def generate_llm_response(history):    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    try:
        stream = client.chat.completions.create(
            model="gpt-4.1-nano",   # Name of the generating model
            messages=history,       # Messages to respond to
            stream=True,            # Stream response as it forms
            temperature=0,          # More deterministic for coding
            n=1,                    # One response per prompt
            presence_penalty=0,     # No bias towards repeated tokens
            frequency_penalty=0,    # No bias towards frequency of tokens
            tools=None,             # Disable tool calling
            modalities=['text'],    # Limit model to generating text
            prediction=None,        # No response template 
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
                
    except Exception as e:
        yield f"Errore durante la generazione: {e}"


def authentication_needed(fn):
    @wraps(fn)
    def implementation(*args, **kwargs):
        if 'fred_logged_in' in session:
            return fn(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return implementation


def is_htmx_request():
    """Check if the request is made by htmx"""
    return request.headers.get('HX-Request') == 'true'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        
        if password == os.getenv('LOGIN_PASSWORD'):
            session['fred_logged_in'] = True

            # To use PERMANENT_SESSION_LIFETIME's session duration
            session.permanent = True
            
            if is_htmx_request():
                # For htmx requests, return empty content with redirect header
                response = make_response('')
                response.headers['HX-Redirect'] = url_for('index')
                return response
            else:
                # For regular form submission, redirect normally
                return redirect(url_for('index'))
        else:
            error_message = "Password errata. Riprova."
            
            if is_htmx_request():
                # Return formatted error HTML for htmx to swap into the error container
                error_html = f'''
                <div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-2xl mb-4 relative animate-pulse" role="alert"
                     x-data="{{ show: false }}" 
                     x-init="setTimeout(() => show = true, 100)"
                     x-show="show"
                     x-transition:enter="transition ease-out duration-300"
                     x-transition:enter-start="opacity-0 transform scale-95"
                     x-transition:enter-end="opacity-100 transform scale-100">
                    <div class="flex items-center">
                        <svg class="w-5 h-5 mr-2 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path>
                        </svg>
                        <span class="font-medium">{error_message}</span>
                    </div>
                </div>
                '''
                return error_html
            else:
                # For regular form submission, use flash messages
                from flask import flash
                flash(error_message, 'error')
                return render_template('login.html')
    
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
    # Get chat history
    history = data['history']
    
    emit('response_start')
    
    try:
        # Generate and stream LLM response using the full history
        for chunk in generate_llm_response(history):
            emit('response_chunk', {'chunk': chunk})
            socketio.sleep(0) # Let socketio manage other connections/events
        
        emit('response_complete')
        
    except Exception as e:
        emit('response_error', {'error': f'{e}'})

# Enable crash logging for both prod and dev
enable_crash_logging('..')

if __name__ == '__main__':
    # Run the application with gevent
    socketio.run(app, debug=True, host='127.0.0.1', port=int(os.getenv('PORT')))