import pickle
import os
import pandas as pd


f=open(r'./路徑/檔名.pkl','rb')
data=pickle.load(f)
# print(data)
pickle_df = pd.read_pickle(r'./路徑/檔名.pkl')
print(pickle_df)
