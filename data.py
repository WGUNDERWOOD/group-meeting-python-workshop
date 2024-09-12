import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("boston.csv")
print(df)
print(df.columns)
df["ONE"] = 1
x_cols = ["ONE", "CRIM", "AGE", "TAX"]
y_col = "MEDV"
df = df[x_cols + [y_col]]
df = df.dropna()
X = df[x_cols]
Y = np.log(df[y_col])

def fit_lm_beta_hat(X, Y):
    K = X.T @ X
    return np.linalg.inv(K) @ X.T @ Y

def get_fitted_values(X, beta_hat):
    return X @ np.array(beta_hat)

beta_hat = fit_lm_beta_hat(X, Y)
print(beta_hat)
print(beta_hat.shape)
print(X.shape)
fitted_values = get_fitted_values(X, beta_hat)
residuals = Y - fitted_values
print(fitted_values)
print(Y)

(fig, ax) = plt.subplots(figsize=(5, 5))
plt.hist(Y)
plt.savefig("y.png")

(fig, ax) = plt.subplots(figsize=(5, 5))
plt.scatter(fitted_values, residuals)
plt.savefig("fitted_values_residuals.png")

(fig, ax) = plt.subplots(figsize=(5, 5))
plt.scatter(fitted_values, Y)
plt.savefig("fitted_values_y.png")
plt.close("all")
