# Diabetes Prediction Web Application

A machine learning powered web application built using Python and Streamlit to predict whether a person is diabetic based on key medical attributes.  
The application uses a trained classification model and provides instant predictions through a simple user friendly interface.

## Table of Contents
1. Overview  
2. Project Objective  
3. Dataset Information  
4. Application Features  
5. Project Structure  
6. Technologies Used  
7. How the Prediction Works  
8. How to Run the Project  
9. Deployment  
10. Author  

## Overview
This project implements a Diabetes Prediction system using a pre trained machine learning model deployed as a Streamlit web application.  
Users can enter health related parameters such as glucose level BMI and age and receive a real time prediction result.

The project demonstrates how a machine learning model can be integrated into an interactive web application for practical healthcare analytics use cases.

## Project Objective
The primary objective of this project is to build an easy to use predictive system that assists in identifying the likelihood of diabetes based on medical input features.  
It focuses on model deployment usability and real time inference rather than model training.

## Dataset Information
The model is trained on a diabetes dataset containing the following features.

1. Number of Pregnancies  
2. Glucose Level  
3. Blood Pressure  
4. Skin Thickness  
5. Insulin Level  
6. Body Mass Index  
7. Diabetes Pedigree Function  
8. Age  

The target variable indicates whether the person is diabetic or not.

## Application Features
1. Simple web based interface built using Streamlit  
2. Accepts real time user input for medical parameters  
3. Loads a pre trained machine learning model using pickle  
4. Performs prediction for a single instance  
5. Displays a clear and human readable prediction result  

## Project Structure
app.py  
trained_model.sav  
requirements.txt  

## Technologies Used
Python  
NumPy  
Scikit Learn  
Streamlit  
Pickle  

## How the Prediction Works
1. User enters medical details in the web interface  
2. Input data is converted into a NumPy array  
3. The array is reshaped to match the model input format  
4. The trained machine learning model predicts the outcome  
5. The application displays whether the person is diabetic or not  

## How to Run the Project
1. Clone the repository  
2. Install dependencies from requirements.txt  
3. Ensure trained_model.sav is present in the project directory  
4. Run the application using Streamlit  

## Deployment
This project can be deployed using Streamlit Community Cloud by selecting app.py as the main application file.

## Author
Satyam Gajjar
