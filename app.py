import subprocess
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
hostname = subprocess.run(['cat', '/etc/hostname'], stdout=subprocess.PIPE).stdout.decode('utf-8')

@app.route('/')
def hello():
    count = redis.incr('hits')
    return '<center><h1>UBT</h2><p>Pershendetje! Kjo faqe eshte vizituar {count} here.</p><br/><p>ID e konteinerit: {hostname}</p></center>'.format(count=count,hostname=hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
