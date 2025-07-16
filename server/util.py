import json
import pickle
import numpy as np
import pandas as pd

__location=None
__data_columns=None
__model=None

def get_estimated_price(sqft,bath,bhk,location):
    try:
        loc_idx=__data_columns.index(location.lower())
    except:
        loc_idx=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_idx>=0:
        x[loc_idx]=1
    return round(__model.predict([x])[0],2)


def get_location_names():
    return __location

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __location

    with open("./artifacts/columns.json","r") as f:
        __data_columns=json.load(f)["data_columns"]
        __location=__data_columns[3:]
    
    global __model
    with open("./artifacts/banglore_home_prices_model.pickle","rb") as f:
        __model=pickle.load(f) 
    print("loading saved artifacts...done")



if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price(1000,2,2,"1st Phase JP Nagar"))
    print(get_estimated_price(1000,3,3,"1st Phase JP Nagar"))
    print(get_estimated_price(1000,2,2,"Kalhali"))
    print(get_estimated_price(1000,2,2,"Ejipura"))