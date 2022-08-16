import pandas as pd
import time
csv=pd.read_csv('Besucherzählung_Ausfallzeit.csv')
#get all the colums from a month
#date=csv['Datum']
#remove day and year from date
#date=date.str.split('.',expand=True)[1]
#get amount of visitors
march={'in':[],'out':[]}
april={'in':[],'out':[]}
may={'in':[],'out':[]}
june={'in':[],'out':[]}
july={'in':[],'out':[]}
august={'in':[],'out':[]}
march_inc=[]
april_inc=[]
may_inc=[]
june_inc=[]
july_inc=[]
august_inc=[]
march_out=[]
april_out=[]
may_out=[]
june_out=[]
july_out=[]
august_out=[]

for row in csv.iterrows():
    date=row[1]['Datum']
    month=date[0:5]
    #get values for first and last day of each month
    if month=='01.03':
        NE1_EIN=row[1]['NE1_EIN']
        NE1_AUS=row[1]['NE1_AUS']
        NE2_EIN=row[1]['NE2_EIN']
        NE2_AUS=row[1]['NE2_AUS']
        HE_EIN=row[1]['HE_EIN']
        HE_AUS=row[1]['HE_AUS']
        march_inc.append(NE1_EIN)
        march_inc.append(NE2_EIN)
        march_inc.append(HE_EIN)
        march_out.append(NE1_AUS)
        march_out.append(NE2_AUS)
        march_out.append(HE_AUS)

#sum all values in a list
march_inc_vis=sum(march_inc)
march_out_vis=sum(march_out)
print(march_inc_vis)
print(march_out_vis)