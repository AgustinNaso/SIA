import csv
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("europe.csv",
                 names=['Country', 'Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment'],
                 skiprows=[0])

model = PCA()

features = ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
countries = df['Country'].tolist()

# Separating out the features
x = df.loc[:, features].values

x = StandardScaler().fit_transform(x)

principalComponents = model.fit_transform(x)

def get_pca_first_components():
    return principalComponents[:, 0]

def get_pca_first_component():
    return model.components_[0]