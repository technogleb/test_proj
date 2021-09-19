from flask import Flask

app = Flask(__name__)


@app.route('/index', strict_slashes=False)
def index():
    return 'app is working'


if __name__ == "__main__":
    app.run('localhost', 5000)
