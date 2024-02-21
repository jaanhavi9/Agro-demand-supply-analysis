from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
