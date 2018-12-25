import subprocess
from flask import Flask
from redis import Redis
from flask import json
from flask import render_template, send_from_directory

app = Flask(__name__, template_folder='templates')

hostname = subprocess.run(['cat', '/etc/hostname'], stdout=subprocess.PIPE).stdout.decode('utf-8')
redis = Redis(host='redis', port=6379)
version = "v1.0"

# Route qe kthen faqen kryesore
@app.route('/')
def hello():
    count = redis.incr('hits')
    return render_template('index.html', version=version, hostname=hostname, count=count)

# Route qe perdoret per healthcheck te aplikacionit nga kubernetes
@app.route('/healthcheck', methods=['POST', 'GET'])
def return_healthcheck():
    data = {'success':True}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# Route qe perdoret per servimin e imazhit ne background
@app.route('/images/<path:path>')
def return_images(path):
    return send_from_directory('templates', path)

# Ngritja e flask serverit
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
