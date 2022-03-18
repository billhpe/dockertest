from flask import Flask
app = Flask(__name__)

def get_message():
    return "Hello unit test"

@app.route('/')
def home():
    return '<h1>' + get_message() + '</h2>'


if __name__ == "__main__":
    app.run(debug=True)
