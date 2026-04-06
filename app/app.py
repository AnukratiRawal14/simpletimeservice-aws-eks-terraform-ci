from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "ip": request.remote_addr
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)