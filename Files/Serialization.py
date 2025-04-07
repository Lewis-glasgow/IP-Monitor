import pickle
import os

def Load():
    return []
    return
    if os.path.exists('C:/data.pkl'):
        with open('data.pkl', 'rb') as f:
             return pickle.load(f)
        
    return []

def Save(data):
    return
    with open('C:/data.pkl', 'wb') as f:
        pickle.dump(data, f)