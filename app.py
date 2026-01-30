from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])

        result = model.predict([[area, bedrooms, bathrooms]])
        prediction = round(result[0], 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)