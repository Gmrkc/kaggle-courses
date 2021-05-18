import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# region_1 and region_2 are pretty uninformative names for locale columns in the dataset.
# Create a copy of reviews with these columns renamed to region and locale, respectively.
renamed = reviews.rename(columns={'region_1' : 'region', 'region_2' : 'locale'})

# Set the index name in the dataset to wines.
reindexed = reviews.rename_axis('wines', axis='rows')

gaming_products = pd.read_csv("gaming.csv")
movie_products = pd.read_csv("movies.csv")

# Create a DataFrame of products mentioned on either dataframe.
combined_products = pd.concat([gaming_products, movie_products])

powerlifting_meets = pd.read_csv("meets.csv")
powerlifting_competitors = pd.read_csv("openpowerlifting.csv")

# Both tables include references to a MeetID, a unique key for each meet (competition) included in the database. 
# Using this, generate a dataset combining the two tables into one.
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))