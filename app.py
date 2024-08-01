from flask import Flask, url_for, render_template
from form import InputForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title= "Home")

@app.route("/predict")
def predict():
    form = InputForm()
    return render_template("predict.html", title="Predict", form= form)

if __name__ == "__main__":
    app.run(debug = True)