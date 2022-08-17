import pandas as pd
import time
csv=pd.read_csv('Python\CSV\Besucherzählung_Ausfallzeit.csv')
März=['01.03.2022','31.03.2022']
April=['01.04.2022','30.04.2022']
Mai=['02.05.2022','31.05.2022']
Juni=['01.06.2022','30.06.2022']
Juli=['01.07.2022','31.07.2022']
monthlist=[März,April,Mai,Juni,Juli]
#search for the first entry in the März list in the csv and return the count
visitcount={}
Märzlist=1
Aprillist=0
Mailist=0
Junilist=0
Julilist=0
for row in csv.iterrows():
    date=row[1]['Datum']
    #print(date)
    month=date[3:5]
    if month == "03":
        Märzlist+=1
    if month=="04":
        Aprillist+=1
    if month=="05":
        Mailist+=1
    if month=="06":
        Junilist+=1
    if month=="07":
        Julilist+=1


Aprillist=Aprillist+Märzlist
Mailist=Mailist+Aprillist
Junilist=Junilist+Mailist
Julilist=Julilist+Junilist



ne1_ein=csv['NE1_EIN']
ne1_aus=csv['NE1_AUS']
ne2_ein=csv['NE2_EIN']
ne2_aus=csv['NE2_AUS']
he_ein=csv['HE_EIN']
he_aus=csv['HE_AUS']
if März[0]== csv['Datum'][0]:
    März_start_e1_in=ne1_ein[0]
    März_start_e2_in=ne2_ein[0]
    März_start_he_in=he_ein[0]
    März_start_e1_out=ne1_aus[0]
    März_start_e2_out=ne2_aus[0]
    März_start_he_out=he_aus[0]
#using Märzlist, get the data at said line
for i in range(Märzlist):
    if März[1]== csv['Datum'][i]:
        März_end_e1_in=ne1_ein[i]
        März_end_e2_in=ne2_ein[i]
        März_end_he_in=he_ein[i]
        März_end_e1_out=ne1_aus[i]
        März_end_e2_out=ne2_aus[i]
        März_end_he_out=he_aus[i]
#mathtime
März_e1_Visitors=März_end_e1_in-März_start_e1_in
März_e2_Visitors=März_end_e2_in-März_start_e2_in
März_he_Visitors=März_end_he_in-März_start_he_in
März_e1_Out=März_end_e1_out-März_start_e1_out
März_e2_Out=März_end_e2_out-März_start_e2_out
März_he_Out=März_end_he_out-März_start_he_out
März_Visitors_in=sum([März_e1_Visitors,März_e2_Visitors,März_he_Visitors])
März_Visitors_out=sum([März_e1_Out,März_e2_Out,März_he_Out])
März_Visitors=max(März_Visitors_in,März_Visitors_out)
visitcount['März']=März_Visitors
print(f'März Visitors: {März_Visitors}')
if April[0]== csv['Datum'][Märzlist+1]:
    April_start_e1_in=ne1_ein[Märzlist+1]
    April_start_e2_in=ne2_ein[Märzlist+1]
    April_start_he_in=he_ein[Märzlist+1]
    April_start_e1_out=ne1_aus[Märzlist+1]
    April_start_e2_out=ne2_aus[Märzlist+1]
    April_start_he_out=he_aus[Märzlist+1]
#using Aprillist, get the data at said line
for i in range(Aprillist):
    if April[1]== csv['Datum'][i]:
        April_end_e1_in=ne1_ein[i]
        April_end_e2_in=ne2_ein[i]
        April_end_he_in=he_ein[i]
        April_end_e1_out=ne1_aus[i]
        April_end_e2_out=ne2_aus[i]
        April_end_he_out=he_aus[i]
#mathtime
April_e1_Visitors=April_end_e1_in-April_start_e1_in
April_e2_Visitors=April_end_e2_in-April_start_e2_in
April_he_Visitors=April_end_he_in-April_start_he_in
April_e1_Out=April_end_e1_out-April_start_e1_out
April_e2_Out=April_end_e2_out-April_start_e2_out
April_he_Out=April_end_he_out-April_start_he_out
April_Visitors_in=sum([April_e1_Visitors,April_e2_Visitors,April_he_Visitors])
April_Visitors_out=sum([April_e1_Out,April_e2_Out,April_he_Out])
April_Visitors=max(April_Visitors_in,April_Visitors_out)
visitcount['April']=April_Visitors
print(f'April Visitors: {April_Visitors}')
if Mai[0] == csv['Datum'][Aprillist+1]:
    Mai_start_e1_in=ne1_ein[Aprillist+1]
    Mai_start_e2_in=ne2_ein[Aprillist+1]
    Mai_start_he_in=he_ein[Aprillist+1]
    Mai_start_e1_out=ne1_aus[Aprillist+1]
    Mai_start_e2_out=ne2_aus[Aprillist+1]
    Mai_start_he_out=he_aus[Aprillist+1]
#using Mailist, get the data at said line
for i in range(Mailist):
    if Mai[1]== csv['Datum'][i]:
        Mai_end_e1_in=ne1_ein[i]
        Mai_end_e2_in=ne2_ein[i]
        Mai_end_he_in=he_ein[i]
        Mai_end_e1_out=ne1_aus[i]
        Mai_end_e2_out=ne2_aus[i]
        Mai_end_he_out=he_aus[i]
#mathtime
Mai_e1_Visitors=Mai_end_e1_in-Mai_start_e1_in
Mai_e2_Visitors=Mai_end_e2_in-Mai_start_e2_in
Mai_he_Visitors=Mai_end_he_in-Mai_start_he_in
Mai_e1_Out=Mai_end_e1_out-Mai_start_e1_out
Mai_e2_Out=Mai_end_e2_out-Mai_start_e2_out
Mai_he_Out=Mai_end_he_out-Mai_start_he_out
Mai_Visitors_in=sum([Mai_e1_Visitors,Mai_e2_Visitors,Mai_he_Visitors])
Mai_Visitors_out=sum([Mai_e1_Out,Mai_e2_Out,Mai_he_Out])
Mai_Visitors=max(Mai_Visitors_in,Mai_Visitors_out)
visitcount['Mai']=Mai_Visitors
print(f'Mai Visitors: {Mai_Visitors}')
if Juni[0]== csv['Datum'][Mailist+1]:
    Juni_start_e1_in=ne1_ein[Mailist+1]
    Juni_start_e2_in=ne2_ein[Mailist+1]
    Juni_start_he_in=he_ein[Mailist+1]
    Juni_start_e1_out=ne1_aus[Mailist+1]
    Juni_start_e2_out=ne2_aus[Mailist+1]
    Juni_start_he_out=he_aus[Mailist+1]
#using Junilist, get the data at said line
for i in range(Junilist):
    if Juni[1]== csv['Datum'][i]:
        Juni_end_e1_in=ne1_ein[i]
        Juni_end_e2_in=ne2_ein[i]
        Juni_end_he_in=he_ein[i]
        Juni_end_e1_out=ne1_aus[i]
        Juni_end_e2_out=ne2_aus[i]
        Juni_end_he_out=he_aus[i]
#mathtime
Juni_e1_Visitors=Juni_end_e1_in-Juni_start_e1_in
Juni_e2_Visitors=Juni_end_e2_in-Juni_start_e2_in
Juni_he_Visitors=Juni_end_he_in-Juni_start_he_in
Juni_e1_Out=Juni_end_e1_out-Juni_start_e1_out
Juni_e2_Out=Juni_end_e2_out-Juni_start_e2_out
Juni_he_Out=Juni_end_he_out-Juni_start_he_out
Juni_Visitors_in=sum([Juni_e1_Visitors,Juni_e2_Visitors,Juni_he_Visitors])
Juni_Visitors_out=sum([Juni_e1_Out,Juni_e2_Out,Juni_he_Out])
Juni_Visitors=max(Juni_Visitors_in,Juni_Visitors_out)
visitcount['Juni']=Juni_Visitors
print(f'Juni Visitors: {Juni_Visitors}')
if Juli[0]== csv['Datum'][Junilist+1]:
    Juli_start_e1_in=ne1_ein[Junilist+1]
    Juli_start_e2_in=ne2_ein[Junilist+1]
    Juli_start_he_in=he_ein[Junilist+1]
    Juli_start_e1_out=ne1_aus[Junilist+1]
    Juli_start_e2_out=ne2_aus[Junilist+1]
    Juli_start_he_out=he_aus[Junilist+1]
#using julist, get the data at said line
for i in range(Julilist):
    if Juli[1]== csv['Datum'][i]:
        Juli_end_e1_in=ne1_ein[i]
        Juli_end_e2_in=ne2_ein[i]
        Juli_end_he_in=he_ein[i]
        Juli_end_e1_out=ne1_aus[i]
        Juli_end_e2_out=ne2_aus[i]
        Juli_end_he_out=he_aus[i]
#mathtime
Juli_e1_Visitors=Juli_end_e1_in-Juli_start_e1_in
Juli_e2_Visitors=Juli_end_e2_in-Juli_start_e2_in
Juli_he_Visitors=Juli_end_he_in-Juli_start_he_in
Juli_e1_Out=Juli_end_e1_out-Juli_start_e1_out
Juli_e2_Out=Juli_end_e2_out-Juli_start_e2_out
Juli_he_Out=Juli_end_he_out-Juli_start_he_out
Juli_Visitors_in=sum([Juli_e1_Visitors,Juli_e2_Visitors,Juli_he_Visitors])
Juli_Visitors_out=sum([Juli_e1_Out,Juli_e2_Out,Juli_he_Out])
Juli_Visitors=max(Juli_Visitors_in,Juli_Visitors_out)
visitcount['Juli']=Juli_Visitors
print(f'Juli Visitors: {Juli_Visitors}')

df=pd.DataFrame(visitcount,index=['Visitors'])
df.to_csv('C:/Users/aky547/GitHub/WorkPrograms/Python/CSV/Besucherzusammenfassung.csv')