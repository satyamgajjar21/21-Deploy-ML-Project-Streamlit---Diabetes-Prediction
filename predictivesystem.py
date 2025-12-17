# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#load the saved model, 
loaded_model = pickle.load(open("/Users/satyamgajjar/Library/Mobile Documents/com~apple~CloudDocs/Satyam's Mac/Learnings/Data Science/Code With Harry - Data Science/14 Practicing ML using Scikit-learn/20 Projects/21 Deploy ML Project Steamlit - Diabetes Prediction/trained_model.sav", "rb"))


input_data = (6,148,72,35,0,33.6,0.627,50)

#changing input array to numpy
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for 1 instance, so that model can know that we are not giving the 768 data
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(f"Output is : {prediction}")

if (prediction[0] == 0):
  print("The person is not diabetic")
else:
  print("The person is diabetic")