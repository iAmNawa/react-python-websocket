from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get-request')
def hello():
    return "get request"

if __name__ == '__main__':
    app.run()
