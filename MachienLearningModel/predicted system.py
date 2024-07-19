# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
loaded_model=pickle.load(open('C:/Users\HP/Desktop/MachienLearningModel/trained_model.sav','rb')) 

# Building Model
input_data=(41,0,1,130,204,0,0,172,0,1.4,2,0,2)

input_data_as_np_array=np.asarray(input_data)

input_data_reshaped = input_data_as_np_array.reshape(1, -1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0==0]):
  print("The Person Does Not Have Heart Disease")
else:
  print("The Person Has Heart Disease")
