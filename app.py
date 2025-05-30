# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, CI/CD with GitHub Actions!'

if __name__ == '__main__':
    app.run(debug=True)