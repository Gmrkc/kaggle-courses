import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# Who are the most common wine reviewers in the dataset? 
# Create a Series whose index is the taster_twitter_handle category from the dataset, 
# and whose values count how many reviews each person wrote.
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# What is the best wine I can buy for a given amount of money? 
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

# What are the minimum and maximum prices for each variety of wine?
price_extremes = reviews.groupby(['variety']).price.agg([min, max])

# What are the most expensive wine varieties?
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

# Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# What combination of countries and varieties are most common?
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
