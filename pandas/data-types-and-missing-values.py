import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# What is the data type of the points column in the dataset?
dtype = reviews.points.dtype

# Create a Series from entries in the points column, but convert the entries to strings.
point_strings = reviews.points.astype('str')

# How many reviews in the dataset are missing a price?
n_missing_prices = pd.isnull(reviews.price).sum()

# What are the most common wine-producing regions? 
# Create a Series counting the number of times each value occurs in the region_1 field.
# This field is often missing data, so replace missing values with Unknown.
# Sort in descending order.
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)