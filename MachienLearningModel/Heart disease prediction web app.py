# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:09:44 2024

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:\\Users\\HP\\Desktop\\MachienLearningModel\\trained_model.sav','rb')) 


#Creating a Function
def heart_prediction(input_data):
    input_data_as_np_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_np_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return "The Person Does Not Have Heart Disease"
    else:
        return "The Person Has Heart Disease"
      
      
      
      
      
      
      
def main():
    
    
    #Giving a Title
    st.title('Heart Disease Prediction')
    
    #Getting The Input Data From The user
    
    
   

# Collecting user inputs


# Input section
import streamlit as st

# Function for prediction
def heart_prediction(inputs):
    # Example of processing and returning a prediction
    # Replace this with your actual prediction logic
    prediction = "Normal"  # Placeholder result
    return prediction

def main():
    # Input fields
    age = st.text_input("Enter Age")
    sex = st.selectbox("Select Sex", ["Male", "Female"])
    resting_blood_pressure = st.text_input("Enter Resting Blood Pressure")
    cholesterol_level = st.text_input("Enter Cholesterol Level")
    fasting_blood_sugar = st.selectbox("Select Fasting Blood Sugar", ["True", "False"])
    resting_ecg_results = st.selectbox("Select Resting ECG Results", ["Normal", "Abnormal"])
    maximum_heart_rate = st.text_input("Enter Maximum Heart Rate")
    exercise_induced_angina = st.selectbox("Select Exercise Induced Angina", ["Yes", "No"])
    st_depression = st.text_input("Enter ST Depression")
    st_slope = st.selectbox("Select ST Slope", ["Up", "Flat", "Down"])
    num_major_vessels = st.text_input("Enter Number of Major Vessels")
    thalassemia_type = st.selectbox("Select Thalassemia Type", ["Normal", "Fixed Defect", "Reversible Defect"])

    # Display the result using a button
    if st.button('Predict'):
        try:
            # Convert inputs to appropriate types
            resting_blood_pressure = float(resting_blood_pressure)
            cholesterol_level = float(cholesterol_level)
            maximum_heart_rate = float(maximum_heart_rate)
            st_depression = float(st_depression)
            num_major_vessels = float(num_major_vessels)
            
            # Assuming binary inputs are converted accordingly
            fasting_blood_sugar = (1 if fasting_blood_sugar == "True" else 0)
            resting_ecg_results = (1 if resting_ecg_results == "Abnormal" else 0)
            exercise_induced_angina = (1 if exercise_induced_angina == "Yes" else 0)
            st_slope_mapping = {"Up": 0, "Flat": 1, "Down": 2}
            st_slope = st_slope_mapping.get(st_slope, 0)  # Default to 0 if not found
            
            # Call prediction function with all inputs
            diagnosis = heart_prediction([age, sex, resting_blood_pressure, cholesterol_level,
                                          fasting_blood_sugar, resting_ecg_results,
                                          maximum_heart_rate, exercise_induced_angina,
                                          st_depression, st_slope, num_major_vessels,
                                          thalassemia_type])
            
            st.write(f"Diagnosis: {diagnosis}")
        
        except ValueError:
            st.error("Please enter valid numeric values for appropriate fields.")

if __name__ == '__main__':
    main()
