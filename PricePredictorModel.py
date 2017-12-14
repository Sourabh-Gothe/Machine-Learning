import pandas as pd
import numpy as np
from sklearn import model_selection, preprocessing, linear_model, pipeline
import seaborn as sns

path = r"https://raw.githubusercontent.com/abulbasar/data/master/kaggle-houseprice/data_combined_cleaned.csv"

df = pd.read_csv(path)
df = df[~np.isnan(df.SalesPrice)]
target = "SalesPrice"
y = df[target]
del df[target]
X = df
df.info()