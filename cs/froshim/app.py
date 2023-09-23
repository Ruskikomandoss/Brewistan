from flask import Flask, render_template, request

app=Flask(__name__)

uczestnicy = {}

sporty = [
    "Koszykówka",
    "Rugby",
    "Boks",
    "Pływanie",
    "Szermierka",
    "Trójbój"
]

@app.route("/")
def index():
    return render_template("index.html", sporty=sporty)


@app.route("/register", methods=["POST"])
def register():
    imie = request.form.get("imie")
    if not imie:
        return render_template("poraszka.html")
    sport = request.form.get("sport")
    if sport not in sporty:
        return render_template("poraszka.html")
    uczestnicy[imie] = sport
    return render_template("success.html")


@app.route("/uczestniczacy")
def uczestniczacy():
    return  render_template("uczestniczacy.html", uczestnicy=uczestnicy)
















if __name__ == '__main__':
    app.run(debug=True)
    print(uczestnicy)