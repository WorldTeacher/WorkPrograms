import pandas as pd

csv=pd.read_csv('Besucherzählung_Ausfallzeit.csv')
#get all the colums from a month
date=csv['Datum']
#remove day and year from date
date=date.str.split('.',expand=True)[0]
date=date.replace()