# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!' # Thay đổi ở đây

if __name__ == '__main__':
    app.run(debug=True)