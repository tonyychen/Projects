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
    year = fields.SelectField('Year', choices = choices_all['choices_years'], validators = [validators.InputRequired()])
    manufacturer = fields.SelectField('Manufacturer', choices = choices_all['choices_manufacturers'], validators = [validators.InputRequired()])
    model = fields.SelectField('Model', choices = choices_all['choices_models'], validators = [validators.InputRequired()])
    fuel = fields.SelectField('Fuel', choices = choices_all['choices_fuels'], validators = [validators.InputRequired()])
    odometer = fields.IntegerField('Odometer', validators = [validators.InputRequired(), validators.NumberRange(min=10, max=250000, message='The value must be between 10 and 250000.')])
    title_status = fields.SelectField('Title Status', choices = choices_all['choices_title_status'], validators = [validators.InputRequired()])
    transmission = fields.SelectField('Transmission', choices = choices_all['choices_transmissions'], validators = [validators.InputRequired()])
    state = fields.SelectField('State', choices = choices_all['choices_states'], validators = [validators.InputRequired()])

#index page
@app.route('/')
def index():
    form = EntryForm()
    return render_template('index.html', form = form)

@app.route('/results', methods = ['POST'])
def results():
    form = EntryForm(request.form)
    if request.method == 'POST' and form.validate():
        year = int(request.form['year'])
        manufacturer = request.form['manufacturer']
        model = request.form['model']
        fuel = request.form['fuel']
        odometer = int(request.form['odometer'])
        title_status = request.form['title_status']
        transmission = request.form['transmission']
        state = request.form['state']
        X = pd.DataFrame({'year': year, 'manufacturer': manufacturer, 'model': model, 
                    'fuel': fuel, 'odometer': odometer, 'title_status': title_status,
                    'transmission': transmission, 'state': state}, index = [0])
        pred = round(estimator.predict(X)[0], 2)
        return render_template('results.html', content = request.form, price = pred)
    return render_template('index.html', form = form)


if __name__ == '__main__':
    app.run()