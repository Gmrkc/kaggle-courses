import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = 'train.csv'
# Read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# print the list of columns in the dataset to find the name of the prediction target
print(home_data.columns)

y = home_data["SalePrice"]

# List of features
feature_names = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF", "FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]

# Select data corresponding to features in feature_names
X = home_data[feature_names]

# Review data
print(X.describe())

# Print the top few lines
print(X.head())

#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state = 1)

# Fit the model
iowa_model.fit(X, y)

# Make predictions
predictions = iowa_model.predict(X)
print(predictions)

print(iowa_model.predict(X.head()))
print(y.head())