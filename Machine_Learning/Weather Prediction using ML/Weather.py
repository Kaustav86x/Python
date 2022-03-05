# regression 

import numpy as np
import pandas as pd 

wea_predict = pd.read_csv('weatherHistory.csv')
wea_predict.info() 
 
X = wea_predict.columns
print(X)
