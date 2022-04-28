import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression 

def price_predict(features):
    clean = pd.read_csv("autoclean.csv")
    clean.drop(["drive-wheels","Unnamed: 0"], axis = 1, inplace=True)
    
    x = clean[['length','width','horsepower', 'curb-weight', 'engine-size', 'highway-L/100km']]
    y = clean['price']
    
    lr = LinearRegression()
    lr.fit(x, y)
    
    item = np.array(features)
    items = item.reshape(1, -1)
    ans = lr.predict(items)
    return ans[0].round(2)