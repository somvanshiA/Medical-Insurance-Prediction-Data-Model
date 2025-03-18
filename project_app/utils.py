
import pickle
import  json
import numpy as np
import pandas as pd
import config


class MedicalInsurance():
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age = age
        self.gender = gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_' + region 

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.linear_model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'rb') as f:
            self.column_data  = json.load(f)


    def get_predict_charges(self):

        self.load_model()

        column_names = self.linear_model.feature_names_in_   # array of features
        region_index =  np.where(column_names == self.region)[0][0]

        test_array = np.zeros(self.linear_model.n_features_in_) # 9 
        
        
        test_array[0] = self.age
        test_array[1] = self.column_data['gender'][self.gender ]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.column_data['smoker'][self.smoker ]
        test_array[region_index] = 1

        print("Test Array >>",test_array)


        predicted_charges = self.linear_model.predict([test_array])

        return predicted_charges       
