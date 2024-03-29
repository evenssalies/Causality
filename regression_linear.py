# Géron (2022, pp.25-26)
#   Ch. 1, section "Instance-based versus model-based learning"

import  matplotlib.pyplot as plt
import  numpy as np
import  pandas as pd

from    sklearn.linear_model import LinearRegression

# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# Visualize the data
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select a linear model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Make a prediction for Cyprus
#   Cyprus' GDP per capita in 2020
X_new = [[37_655.2]]
print(model.predict(X_new))

# Instance-based learning (k-nearest neighbors)
from    sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=3)

# Train the new model
model.fit(X, y)

# Make a prediction for Cyprus
#   Cyprus' GDP per capita in 2020
X_new = [[37_655.2]]
print(model.predict(X_new))
