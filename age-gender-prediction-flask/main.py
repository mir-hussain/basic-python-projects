from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def main():
    return '<h1>Hello There</h1>'


@app.route("/guess/<name>")
def guess(name):

    ageData = requests.get(f"https://api.agify.io?name={name}")
    ageData.raise_for_status()

    age = ageData.json()['age']
    print(age)

    genderData = requests.get(f"https://api.genderize.io?name={name}")
    genderData.raise_for_status()

    gender = genderData.json()['gender']
    print(gender)

    return render_template("index.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
