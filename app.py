from unittest import result
from flask import Flask, render_template, request, jsonify, session, url_for
from apis import api_1_shazam
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api_1', methods=['GET'])
def api_1():
    return render_template('api.html')

# This route actually runs the API function
# and returns the response.
@app.route('/api_1_run', methods=['POST'])
def api_1_run():
    if session.get('api_used'):
        return jsonify({"error": "This API has already been used."}), 403

    result = api_1_shazam()
    session['api_used'] = True  
    return jsonify(result)

@app.route('/reset')
def reset_api_session():
    session.pop('api_used', None)  # Remove the 'api_used' flag
    return "✅ Session reset. Return to <a href='/'>home</a>."
