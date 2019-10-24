from predictor import EnsembleBuilder
from train_driver import TrainDriver
from flask import Flask, render_template, url_for, request
import os


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/train")
def train():
    td = TrainDriver()
    done = td.driver()
    return(done)

@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    #Making Predictions
    if request.method == 'POST':
        recogspeech = request.form['RecognisedSpeech']  
        eb = EnsembleBuilder()
        result = eb.make_prediction(recogspeech)
        print(result, recogspeech)
        return render_template('predict.html', result=result, speech=recogspeech)

if __name__ == '__main__':
    app.run(debug = True)



