from flask import Flask, render_template, request
import numpy as np
import pickle
#import joblib
app = Flask(__name__)
filename = 'file_week3.pkl'
model = pickle.load(open(filename, 'rb'))    # load the model
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])  # The user input is processed here
def predict():
    fixed_acidity = request.form['fixed acidity']
    citric_acid = request.form['citric acid']
    density = request.form['density']
    pH = request.form['pH']
    sulphates = request.form['sulphates']
    #quality= request.form['quality']
    pred = model.predict(np.array([[fixed_acidity,citric_acid,density,pH,sulphates ]]).astype(float))[0]
    #print(pred)
    return render_template('index.html', predict=str(pred))
if __name__ == '__main__':
    app.run(debug=True)

