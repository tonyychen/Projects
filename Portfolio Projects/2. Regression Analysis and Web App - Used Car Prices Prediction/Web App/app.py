from flask import Flask, render_template, request
from wtforms import Form, fields, validators

import joblib
import os

from feature_selector import FeatureSelector

#Initialize App
app = Flask(__name__)

cur_dir = os.path.dirname(__file__)
estimator = joblib.load(os.path.join(cur_dir, 'joblib_objects', 'best_estimator.joblib'))