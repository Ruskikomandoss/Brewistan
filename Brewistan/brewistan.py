from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/mainpage")
def elo():
    name = request.args.get("name")
    return render_template("mainpage.html", placeholder=name)


@app.route("/store")
def store():
    return render_template("Store.html")


if __name__ == '__main__':
    app.run(debug=True)