import subprocess
from flask import Flask
from flask import render_template, send_from_directory

app = Flask(__name__, template_folder='templates')

hostname = subprocess.run(['cat', '/etc/hostname'], stdout=subprocess.PIPE).stdout.decode('utf-8')
version = "v1.0"

@app.route('/')
def hello():
	return render_template('index.html', version=version, hostname=hostname)

@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory('templates', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
