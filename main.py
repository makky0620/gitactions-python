from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    hello = "Hello world"
    return hello


if __name__ == "__main__":
    app.run()


def plus(x: int, y: int) -> int:
    return x + y


def minus(x: int, y: int) -> int:
    return x - y


def mul(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> int:
    return x / y
