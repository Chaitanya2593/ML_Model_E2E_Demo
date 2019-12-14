# How this works:
#
# 1. Assume the input is present in a local file (if the web service accepts input)
# 2. Upload the file to an Azure blob - you"d need an Azure storage account
# 3. Call BES to process the data in the blob.
# 4. The results get written to another Azure blob.
# 5. Download the output blob to a local file
#
# Note: You may need to download/install the Azure SDK for Python.
# See: http://azure.microsoft.com/en-us/documentation/articles/python-how-to-install/
# Import Required Packages
import urllib.request
import json
import time

from django.conf import settings
import pyodbc
import pandas as pd
from  sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

class Predictor(object):
    def __init__(self):
        '''
        constructore instialation
        '''

    def process_outputfile_1(self, dataframe):
        'Handling python file '
        output = json.loads(dataframe[dataframe['Left']==1].to_json())
        output_ns = json.loads(dataframe[dataframe['Left']==0].to_json())
        return output, output_ns


  
    def predict_function(self, file_path):
        print(file_path)
      #file from the front end    
#         data = pd.read_csv(file_path)
        try:
            data = pd.read_csv(file_path)
            data_2 = pd.read_csv(file_path)
        except:
            AssertionError ("file is not having correct pattern")      
        # dummification by encoding 
        from  sklearn.preprocessing import LabelEncoder
        encoding_list = ['department','salary']
        data[encoding_list] = data[encoding_list].apply(LabelEncoder().fit_transform)
              
              
        model_1 = pickle.load(open(r'C:\Users\chait\Desktop\Data Science UPX\Nestle SFTP\HR_Predictor\polls\HR_model.pkl','rb'))
        data['Left'] = model_1.predict(data)
        data_2["Left"] = data["Left"].apply(lambda x : 0 if x <= 0.5 else 1)
        print(data_2)
        return self.process_outputfile_1(data_2)



