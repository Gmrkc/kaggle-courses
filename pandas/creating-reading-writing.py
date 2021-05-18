import pandas as pd

fruits = pd.DataFrame({'Apples' : [30], 'Bananas' : [21]})

fruit_sales = pd.DataFrame({'Apples' : [35, 41], 'Bananas' : [21, 34]}, index = ['2017 Sales', '2018 Sales'])

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])

animals.to_csv("cows_and_goats.csv")

animals_csv = pd.read_csv('cows_and_goats.csv', index_col=0)