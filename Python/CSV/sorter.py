import pandas as pd
import time
csv=pd.read_csv('/home/alexander/GitHub/WorkPrograms/Python/CSV/Besucherzählung_Ausfallzeit.csv')
march=['01.03.2022','31.03.2022']
april=['01.04.2022','30.04.2022']
may=['02.05.2022','31.05.2022']
june=['01.06.2022','30.06.2022']
july=['01.07.2022','31.07.2022']
august=['01.08.2022','16.08.2022']
monthlist=[march,april,may,june,july,august]
#search for the first entry in the march list in the csv and return the count
visitcount={}
marchlist=1
aprillist=0
maylist=0
junelist=0
julylist=0
augustlist=0
for row in csv.iterrows():
    date=row[1]['Datum']
    #print(date)
    month=date[3:5]
    if month == "03":
        marchlist+=1
    if month=="04":
        aprillist+=1
    if month=="05":
        maylist+=1
    if month=="06":
        junelist+=1
    if month=="07":
        julylist+=1
    if month=="08":
        augustlist+=1

aprillist=aprillist+marchlist
maylist=maylist+aprillist
junelist=junelist+maylist
julylist=julylist+junelist
augustlist=augustlist+julylist


ne1_ein=csv['NE1_EIN']
ne1_aus=csv['NE1_AUS']
ne2_ein=csv['NE2_EIN']
ne2_aus=csv['NE2_AUS']
he_ein=csv['HE_EIN']
he_aus=csv['HE_AUS']
if march[0]== csv['Datum'][0]:
    march_start_e1_in=ne1_ein[0]
    march_start_e2_in=ne2_ein[0]
    march_start_he_in=he_ein[0]
    march_start_e1_out=ne1_aus[0]
    march_start_e2_out=ne2_aus[0]
    march_start_he_out=he_aus[0]
#using marchlist, get the data at said line
for i in range(marchlist):
    if march[1]== csv['Datum'][i]:
        march_end_e1_in=ne1_ein[i]
        march_end_e2_in=ne2_ein[i]
        march_end_he_in=he_ein[i]
        march_end_e1_out=ne1_aus[i]
        march_end_e2_out=ne2_aus[i]
        march_end_he_out=he_aus[i]
#mathtime
March_e1_Visitors=march_end_e1_in-march_start_e1_in
March_e2_Visitors=march_end_e2_in-march_start_e2_in
March_he_Visitors=march_end_he_in-march_start_he_in
March_e1_Out=march_end_e1_out-march_start_e1_out
March_e2_Out=march_end_e2_out-march_start_e2_out
March_he_Out=march_end_he_out-march_start_he_out
March_Visitors_in=sum([March_e1_Visitors,March_e2_Visitors,March_he_Visitors])
March_Visitors_out=sum([March_e1_Out,March_e2_Out,March_he_Out])
March_Visitors=max(March_Visitors_in,March_Visitors_out)
visitcount['march']=March_Visitors
print(f'March Visitors: {March_Visitors}')
if april[0]== csv['Datum'][marchlist+1]:
    april_start_e1_in=ne1_ein[marchlist+1]
    april_start_e2_in=ne2_ein[marchlist+1]
    april_start_he_in=he_ein[marchlist+1]
    april_start_e1_out=ne1_aus[marchlist+1]
    april_start_e2_out=ne2_aus[marchlist+1]
    april_start_he_out=he_aus[marchlist+1]
#using aprillist, get the data at said line
for i in range(aprillist):
    if april[1]== csv['Datum'][i]:
        april_end_e1_in=ne1_ein[i]
        april_end_e2_in=ne2_ein[i]
        april_end_he_in=he_ein[i]
        april_end_e1_out=ne1_aus[i]
        april_end_e2_out=ne2_aus[i]
        april_end_he_out=he_aus[i]
#mathtime
April_e1_Visitors=april_end_e1_in-april_start_e1_in
April_e2_Visitors=april_end_e2_in-april_start_e2_in
April_he_Visitors=april_end_he_in-april_start_he_in
April_e1_Out=april_end_e1_out-april_start_e1_out
April_e2_Out=april_end_e2_out-april_start_e2_out
April_he_Out=april_end_he_out-april_start_he_out
April_Visitors_in=sum([April_e1_Visitors,April_e2_Visitors,April_he_Visitors])
April_Visitors_out=sum([April_e1_Out,April_e2_Out,April_he_Out])
April_Visitors=max(April_Visitors_in,April_Visitors_out)
visitcount['april']=April_Visitors
print(f'April Visitors: {April_Visitors}')
if may[0] == csv['Datum'][aprillist+1]:
    may_start_e1_in=ne1_ein[aprillist+1]
    may_start_e2_in=ne2_ein[aprillist+1]
    may_start_he_in=he_ein[aprillist+1]
    may_start_e1_out=ne1_aus[aprillist+1]
    may_start_e2_out=ne2_aus[aprillist+1]
    may_start_he_out=he_aus[aprillist+1]
#using maylist, get the data at said line
for i in range(maylist):
    if may[1]== csv['Datum'][i]:
        may_end_e1_in=ne1_ein[i]
        may_end_e2_in=ne2_ein[i]
        may_end_he_in=he_ein[i]
        may_end_e1_out=ne1_aus[i]
        may_end_e2_out=ne2_aus[i]
        may_end_he_out=he_aus[i]
#mathtime
May_e1_Visitors=may_end_e1_in-may_start_e1_in
May_e2_Visitors=may_end_e2_in-may_start_e2_in
May_he_Visitors=may_end_he_in-may_start_he_in
May_e1_Out=may_end_e1_out-may_start_e1_out
May_e2_Out=may_end_e2_out-may_start_e2_out
May_he_Out=may_end_he_out-may_start_he_out
May_Visitors_in=sum([May_e1_Visitors,May_e2_Visitors,May_he_Visitors])
May_Visitors_out=sum([May_e1_Out,May_e2_Out,May_he_Out])
May_Visitors=max(May_Visitors_in,May_Visitors_out)
visitcount['may']=May_Visitors
print(f'May Visitors: {May_Visitors}')
if june[0]== csv['Datum'][maylist+1]:
    june_start_e1_in=ne1_ein[maylist+1]
    june_start_e2_in=ne2_ein[maylist+1]
    june_start_he_in=he_ein[maylist+1]
    june_start_e1_out=ne1_aus[maylist+1]
    june_start_e2_out=ne2_aus[maylist+1]
    june_start_he_out=he_aus[maylist+1]
#using junelist, get the data at said line
for i in range(junelist):
    if june[1]== csv['Datum'][i]:
        june_end_e1_in=ne1_ein[i]
        june_end_e2_in=ne2_ein[i]
        june_end_he_in=he_ein[i]
        june_end_e1_out=ne1_aus[i]
        june_end_e2_out=ne2_aus[i]
        june_end_he_out=he_aus[i]
#mathtime
June_e1_Visitors=june_end_e1_in-june_start_e1_in
June_e2_Visitors=june_end_e2_in-june_start_e2_in
June_he_Visitors=june_end_he_in-june_start_he_in
June_e1_Out=june_end_e1_out-june_start_e1_out
June_e2_Out=june_end_e2_out-june_start_e2_out
June_he_Out=june_end_he_out-june_start_he_out
June_Visitors_in=sum([June_e1_Visitors,June_e2_Visitors,June_he_Visitors])
June_Visitors_out=sum([June_e1_Out,June_e2_Out,June_he_Out])
June_Visitors=max(June_Visitors_in,June_Visitors_out)
visitcount['june']=June_Visitors
print(f'June Visitors: {June_Visitors}')
if july[0]== csv['Datum'][junelist+1]:
    july_start_e1_in=ne1_ein[junelist+1]
    july_start_e2_in=ne2_ein[junelist+1]
    july_start_he_in=he_ein[junelist+1]
    july_start_e1_out=ne1_aus[junelist+1]
    july_start_e2_out=ne2_aus[junelist+1]
    july_start_he_out=he_aus[junelist+1]
#using julist, get the data at said line
for i in range(julylist):
    if july[1]== csv['Datum'][i]:
        july_end_e1_in=ne1_ein[i]
        july_end_e2_in=ne2_ein[i]
        july_end_he_in=he_ein[i]
        july_end_e1_out=ne1_aus[i]
        july_end_e2_out=ne2_aus[i]
        july_end_he_out=he_aus[i]
#mathtime
July_e1_Visitors=july_end_e1_in-july_start_e1_in
July_e2_Visitors=july_end_e2_in-july_start_e2_in
July_he_Visitors=july_end_he_in-july_start_he_in
July_e1_Out=july_end_e1_out-july_start_e1_out
July_e2_Out=july_end_e2_out-july_start_e2_out
July_he_Out=july_end_he_out-july_start_he_out
July_Visitors_in=sum([July_e1_Visitors,July_e2_Visitors,July_he_Visitors])
July_Visitors_out=sum([July_e1_Out,July_e2_Out,July_he_Out])
July_Visitors=max(July_Visitors_in,July_Visitors_out)
visitcount['july']=July_Visitors
print(f'July Visitors: {July_Visitors}')

df=pd.DataFrame(visitcount,index=['Visitors'])
df.to_csv('/home/alexander/GitHub/WorkPrograms/Python/CSV/visitors.csv')