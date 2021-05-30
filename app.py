from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("page1.html", content="base")


@app.route('/test')
def test():
    return render_template("test.html")


if __name__ == '__main__':
    app.run()
