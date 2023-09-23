from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("elo.html", name=request.form.get("name", "mordunio"))



# To jest alternatywnie rozpisane na dwie funkcje, powyżej streszczone w jednej
# @app.route("/elo", methods=["GET", "POST"])
# def elo(): JEŚLI MAMY GET, MUSI BYĆ ARGS.GET, 
#     return render_template("elo.html", name = request.args.get("name", "gościu"))


if __name__ == '__main__':
    app.run(debug=True)