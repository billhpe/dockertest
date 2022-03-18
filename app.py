from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Flask app alive and well</h2>'


if __name__ == "__main__":
    app.run(debug=True)
