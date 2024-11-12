from flask import Flask
from datetime import datetime
import os
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = 'Pallapotu Aditya Vardhan'  
    username = os.getenv('USER', 'unknown user')
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.check_output(['top', '-bn', '1']).decode('utf-8')
    return f'<h1>System Information</h1><p>Name: {name}</p><p>Username: {username}</p><p>Server Time: {time}</p><pre>{top_output}</pre>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
