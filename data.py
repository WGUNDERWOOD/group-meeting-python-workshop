import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Boston housing data
df = pd.read_csv("boston.csv")
print(df)
print(df.columns)
# Add unit column for regression intercept
df["ONE"] = 1
# Choose some covariates
x_cols = ["ONE", "CRIM", "AGE", "TAX"]
# Response variable is (log) median price
y_col = "MEDV"
# Drop unnecessary columns
df = df[x_cols + [y_col]]
# Drop rows with missing entries
df = df.dropna()
# Set up design matrix and response vector
X = df[x_cols]
Y = np.log(df[y_col])

def fit_lm_beta_hat(X, Y):
    # Matrix operations to find (X.T X)^(-1) X.T Y
    K = X.T @ X
    return np.linalg.inv(K) @ X.T @ Y

def get_fitted_values(X, beta_hat):
    # Compute X beta_hat
    return X @ np.array(beta_hat)

beta_hat = fit_lm_beta_hat(X, Y)
print(beta_hat)
fitted_values = get_fitted_values(X, beta_hat)
residuals = Y - fitted_values

# Histogram of responses
(fig, ax) = plt.subplots(figsize=(5, 5))
plt.hist(Y)

# Residuals vs fitted values plot
(fig, ax) = plt.subplots(figsize=(5, 5))
plt.scatter(fitted_values, residuals, color="red", marker="x", s=40.0)
plt.xlim([1, 4])
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title("Residuals vs. Fitted Values")
# Can also save as pdf etc
plt.savefig("plot.png")
