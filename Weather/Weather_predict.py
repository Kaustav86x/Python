import numpy as np
import pandas as pd 

# loading the dataset 
wea_predict = pd.read_csv('weatherHistory.csv')
wea_predict.info() 

# showing the columns 
X = wea_predict.columns
print(X)
