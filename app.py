#The main file
from flask import Flask,request, url_for, redirect, render_template
import joblib,os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("phishing.html")   

@app.route('/predict',methods=['POST'])
def predict():
    phish_model = open('phishing.pkl','rb')
    phish_model_ls = joblib.load(phish_model)
    urlName=request.form.get('urlName')
    urlNameStrip=urlName.strip()
    urlReplace=str(urlNameStrip).replace('https://','').replace('http://','')
    predictUrl=[urlReplace]
    prediction=phish_model_ls.predict(predictUrl)

    if predictUrl==['']:
        return render_template('phishing.html',pred='-Field Empty-')
    elif prediction==['good']:
        return render_template('phishing.html',pred='Secure',urlDisplay=[urlNameStrip])
    elif prediction==['bad']:
        return render_template('phishing.html',pred='Not Secure',urlDisplay=[urlNameStrip])


if __name__ == '__main__':
    app.run(debug=True)






