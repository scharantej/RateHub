 
# main.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database to store rate data
rates_db = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
    # Collect user input from the form
    hourly_rate = request.form.get('hourly_rate')
    level = request.form.get('level')
    location = request.form.get('location')
    supplier = request.form.get('supplier')

    # Store the rate data in the database
    rates_db.append({
        'hourly_rate': hourly_rate,
        'level': level,
        'location': location,
        'supplier': supplier
    })

    # Redirect to the results page
    return redirect(url_for('results'))

@app.route('/results')
def results():
    # Retrieve the rate data from the database
    rates = rates_db

    # Calculate the comparison results
    same_level_rates = [rate for rate in rates if rate['level'] == rates[0]['level']]
    same_location_rates = [rate for rate in rates if rate['location'] == rates[0]['location']]
    mixed_rates = [rate for rate in rates if rate['level'] != rates[0]['level'] or rate['location'] != rates[0]['location']]

    # Render the results page with the comparison results
    return render_template('results.html', same_level_rates=same_level_rates, same_location_rates=same_location_rates, mixed_rates=mixed_rates)

if __name__ == '__main__':
    app.run(debug=True)
