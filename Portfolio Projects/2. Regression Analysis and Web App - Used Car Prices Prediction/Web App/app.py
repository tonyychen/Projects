from flask import Flask, render_template, request
from wtforms import Form, fields, validators

import joblib
import os
import pandas as pd

from feature_selector import FeatureSelector

#Initialize App
app = Flask(__name__)

cur_dir = os.path.dirname(__file__)
estimator = joblib.load(os.path.join(cur_dir, 'joblib_objects', 'best_estimator.joblib'))
choices_all = joblib.load(os.path.join(cur_dir, 'joblib_objects', 'choices.joblib'))

#Build Form
class EntryForm(Form):
    year = fields.SelectField('Year', choices = choices_all['choices_years'], coerce = int, validators = [validators.InputRequired('Please select a value.')])
    manufacturer = fields.SelectField('Manufacturer', choices = choices_all['choices_manufacturers'], validators = [validators.InputRequired('Please select a value.')])
    model = fields.SelectField('Model', choices = choices_all['choices_models'], validators = [validators.InputRequired('Please select a value.')])
    fuel = fields.SelectField('Fuel', choices = choices_all['choices_fuels'], validators = [validators.InputRequired('Please select a value.')])
    odometer = fields.IntegerField('Odometer', validators = [validators.InputRequired('Please input a value.'), validators.NumberRange(min=10, max=250000, message='The value must be between 10 and 250000.')])
    title_status = fields.SelectField('Title_status', choices = choices_all['choices_title_status'], validators = [validators.InputRequired('Please select a value.')])
    transmission = fields.SelectField('Transmission', choices = choices_all['choices_transmissions'], validators = [validators.InputRequired('Please select a value.')])
    state = fields.SelectField('State', choices = choices_all['choices_states'], validators = [validators.InputRequired('Please select a value.')])

#index page
@app.route('/')
def index():
    form = EntryForm()
    return render_template('index.html', form = form)

@app.route('/results', methods = ['POST'])
def results():
    form = EntryForm(request.form)
    if request.method = 'POST' and form.validate():
        year = request.form['Year']
        manufacturer = request.form['Manufacturer']
        model = request.form['Model']
        fuel = request.form['Fuel']
        odometer = request.form['Odometer']
        title_status = request.form['Title_status']
        transmission = request.form['Transmission']
        state = request.form['State']
        X = pd.DataFrame({'year': year, 'manufacturer': manufacturer, 'model': model, 
                    'fuel': fuel, 'odometer': odometer, 'title_status': title_status,
                    'transmission': transmission, 'state': state})
        pred = round(estimator.predict(X)[0], 2)
        return render_template('results.html', content = request.form, price = pred)
    return render_template('index.html', form = form)


if __name__ == '__main__':
    app.run()