from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd 
import matplotlib.pyplot as plt
from io import StringIO

app = Flask(__name__)

weather_df = pd.read_csv('next30.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_prices', methods=['GET', 'POST'])
def get_prices():
    if request.method == 'POST':
        commodity_name = request.form['commodity_name']
        num_days = request.form['num_days']
        # Pass the data to FastAPI endpoint
        response = requests.post('http://localhost:8000/predict_prices', json={'commodity_name': commodity_name, 'num_days': num_days})
        # Assuming FastAPI returns JSON response
        data = response.json()
        return render_template('price.html', data=data)
    return render_template('input_form.html')

@app.route('/weather_forecast', methods=['GET'])
def weather_forecast():
    return render_template('weatherforecast.html')

@app.route('/plot_weather', methods=['POST'])
def plot_weather():
    days = int(request.form['days'])
    if days == 15:
        weather_subset = weather_df.head(15)
    elif days == 30:
        weather_subset = weather_df.head(30)
    else:
        return "Invalid number of days"

    plt.plot(weather_subset['Date'], weather_subset['temp'])
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title(f'Weather Forecast for {days} days')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_img = StringIO()
    plt.savefig(plot_img, format='png')
    plot_img.seek(0)
    return plot_img.getvalue(), 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(debug=True)
