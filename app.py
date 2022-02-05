from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "tres hilos sv wip"


if __name__ == "__main__":
    app.run(debug=True)
