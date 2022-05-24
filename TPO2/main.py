import csv
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Referencia: https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

df = pd.read_csv("europe.csv",
                 names=['Country', 'Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment'],
                 skiprows=[0])

model = PCA()

features = ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
countries = df['Country'].tolist()

# Separating out the features
x = df.loc[:, features].values

x = StandardScaler().fit_transform(x)


def get_mean(x, countries):
    for i, val in enumerate(x):
        print(f"COUNTRY: {countries[i]}")
        print(x[i])
        print("----------------------------")
        print(f"MEAN: {val.mean()}")
        print("----------------------------")
        x[i] = val - val.mean()
        print(x[i])
        print("----------------------------")
    return x


# x = get_mean(x,countries)
principalComponents = model.fit_transform(x)


def myplot(score, coeff, labels_features=None, labels_points=None):
    xs = score[:, 0]
    ys = score[:, 1]
    n = coeff.shape[0]
    scalex = 1.0 / (xs.max() - xs.min())
    scaley = 1.0 / (ys.max() - ys.min())
    plt.scatter(xs * scalex, ys * scaley, c=ys)
    for i in range(n):
        plt.arrow(0, 0, coeff[i, 0], coeff[i, 1], color='black', alpha=0.5)
        if labels_features is None:
            plt.text(coeff[i, 0] * 1.15, coeff[i, 1] * 1.15, "Var" + str(i + 1), color='black', ha='center',
                     va='center')
        else:
            plt.text(coeff[i, 0] * 1.15, coeff[i, 1] * 1.15, labels_features[i], color='black', ha='center',
                     va='center')
    if labels_points is not None:
        for i in range(len(xs)):
            plt.text(xs[i] * scalex * 1.15, ys[i] * scaley * 1.15, labels_points[i], color='m', ha='center',
                     va='center')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.grid()


print(model.explained_variance_ratio_)
# print(model.components_[0:2, :])
for i in range(2):
    print(f"PC{i + 1}")
    for j in range(len(model.components_[i])):
        print(f"y{j}: {model.components_[i, j]} - {features[j]}")
# Call the function. Use only the 2 PCs.
myplot(principalComponents[:, 0:2], np.transpose(model.components_[0:2, :]), labels_features=features,
       labels_points=countries)
plt.show()
