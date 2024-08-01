import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (SelectField, DateField, TimeField,IntegerField, SubmitField)
from wtforms.validators import DataRequired
#importing data
train = pd.read_csv("https://raw.githubusercontent.com/MisbahullahSheriff/sagemaker-flight-prices-prediction/master/data/train.csv")
val = pd.read_csv("https://raw.githubusercontent.com/MisbahullahSheriff/sagemaker-flight-prices-prediction/master/data/val.csv")
X_data = pd.concat([train, val], axis = 0).drop(columns = "price")

class InputForm(FlaskForm):
    airline = SelectField(
        label= "Airline",
        choices= X_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )
    
    data_of_journey = DateField(
        label="Date of journey",
        validators=[DataRequired()],
        format='%Y-%m-%d'
    )
    
    source = SelectField(
        label= "Origin of flight",
        choices= X_data.source.unique().tolist(),
        validators=[DataRequired()],
        description="Select the origin of the flight"
    )
    
    destination = SelectField(
        label="Destination",
        choices=X_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )
    
    dep_time = TimeField(
        label= "Departure Time",
        validators=[DataRequired()]
    )
    
    arr_time = TimeField(
        label = "Arrival Time",
        validators=[DataRequired()]
    )
    
    duration = IntegerField(
       label= "Duration of the flight",
       validators=[DataRequired()] 
    )
    
    total_stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    
    additional_onfo = SelectField(
        label="Additional Info",
        choices= X_data.additional_info
    )
    
    submit = SubmitField("Predict")
    