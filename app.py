#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 12:52:32 2025

@author: satyamgajjar
"""

import numpy as np
import pickle
import streamlit as st

# Load model (relative path for deployment)
loaded_model = pickle.load(open("trained_model.sav", "rb"))

# Prediction function
def diabetes_prediction(input_data):
    
    #changing input array to numpy
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    #reshape the array as we are predicting for 1 instance, so that model can know that we are not giving the 768 data
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"

def main():

    st.title("Diabetes Prediction Web Application")

    #getting the input data from user
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of the person")

    #To store result
    diagnosis = ''
    
    #creating a button for prediction
    if st.button("Diabetes Test Result"):
        try:
            diagnosis = diabetes_prediction([
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age
            ])
            st.success(diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values in all fields")

if __name__ == "__main__":
    main()
