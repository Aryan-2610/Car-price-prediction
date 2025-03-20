from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('LinearRegressionModel.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract data from the form
        data = pd.DataFrame([[
            request.form['Company'],
            request.form['Model'],
            request.form['Year'],
            request.form['Kms'],
            request.form['Fuel'],
            request.form['Owner']
        ]], columns=['Company', 'Model', 'Year', 'Kms', 'Fuel', 'Owner'])

        # Predict using the model
        prediction = model.predict(data)[0]

        return render_template('index.html', prediction_text=f'Estimated Price: ₹{prediction:,.2f}')

if __name__ == '__main__':
    app.run(debug=True)
