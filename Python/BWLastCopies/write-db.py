
import sqlite3
from time import sleep
import json5 as json
import glob
'''
jsonfile="C:/Users/aky547/GitHub/isil/data/DE-Frei129.json"
json_count=glob.glob("C:/Users/aky547/GitHub/isil/data/*.json")
count=0
for file in json_count:
    count=count+1
    #print(file, count)'''
def extract_data(jsonfile):
    fields={'001A','001B','001D','001U','002@','003@','008H','009Q','029@','029A','032P','035B','035E','035I','047A','035G','035Q','035P','035D','035L','035O','029R','035H','035J','035K','007N','035M','035N'}
    with open(jsonfile, "r", encoding="utf-8") as f:
        data = json.load(f)

    
    metadata=data['data']
    for field in metadata:
        if field in fields:
            if field == '008H':
                adressdata=metadata[field][0]
                for entry in adressdata:
                    for key in entry:
                        if key == 'a' is not None: 
                            zdb=entry[key]
                        else: zdb=None
                        if key == 'b' is not None:
                            dbs=entry[key]
                        else: dbs=None
                        if key == 'd' is not None:
                            sigel=entry[key]
                        else: sigel=None
                        if key == 'e' is not None:
                            isil=entry[key]
                        else: isil=None
                        if key == 'f' is not None:
                            ezb=entry[key]
                        else: ezb=None

            if field =='009Q':
                    for content in metadata[field]:
                        temp_dict = {k:v for subdict in content for k, v in subdict.items()} 
                        if temp_dict.get("z", None) == 'A':
                            homepage=temp_dict.get("u", None)
                        if temp_dict.get("z", None) == 'B':
                            opac=temp_dict.get("u", None)
            if field =='029@':
                namedata=metadata[field][0]
                for entry in namedata:
                    for key in entry:
                        if key =='a':
                            shortname=entry[key]
            if field =='029A':
                namedata=metadata[field][0]
                for entry in namedata:
                    for key in entry:
                        if key =='a':
                            longname=entry[key]
            if field == '032P':
                sigildata=metadata[field][0]
                for entry in sigildata:
                    #entries are like this {'a': 'Kunzenweg 21'}
                    # based on identifier, get value
                    for key in entry:
                        if key == 'a':
                            street=entry[key]
                        elif key == 'b':
                            city=entry[key]
                        elif key == 'd':
                            country=entry[key]
                        elif key == 'e':
                            zip=entry[key]
                        elif key == 'f':
                            state=entry[key]
            if field == '035B':
                maildata=metadata[field][0]
                for entry in maildata:
                    for key in entry:
                        '''if key == 'd':
                            phone_country=entry[key]
                        if key == 'e':
                            phone_city=entry[key]
                        if key == 'f':
                            phone_number=entry[key]
                        #if keys d, e, f  exist, create phone number
                        if phone_country and phone_city and phone_number != None:
                            phone=f'+{phone_country} {phone_city}{phone_number}'
                        else:
                            phone=None'''
                        if key == 'k':
                            mail=entry[key]
                            print(mail)
                        
                
            
                
            if field == '035E':
                typedata=metadata[field][0]
                for entry in typedata:
                    for key in entry:
                        if key == 'f':
                            orgatype=entry[key]
    
    #print(phone, mail)   
    print(zdb, dbs, sigel, isil, ezb, homepage, opac, street, city, country, zip, state, shortname, longname, orgatype,phone, mail)     
    return zdb, dbs, sigel, isil, ezb, homepage, opac, street, city, country, zip, state,shortname,longname,orgatype, phone, mail
def connect_database():
    conn = sqlite3.connect('sigel.db')
    c = conn.cursor()
    return c, conn
def write_database():
    count=0
    for file in glob.glob("C:/Users/aky547/GitHub/isil/data/*.json"):
        count=count+1
        jsonfile=file
    
    zdb, dbs, sigel, isil, ezb, homepage, opac, street, city, country, zip, state, shortname, longname, orgatype,phone, mail = extract_data(jsonfile)
    print(zdb, dbs, sigel, isil, ezb, homepage, opac, street, city, country, zip, state, shortname, longname, orgatype,phone, mail)
    c, conn = connect_database()
    
    
    c.execute("INSERT INTO data VALUES(?,?,?,?)", (count,shortname,longname,orgatype))
    c.execute("INSERT INTO sigil VALUES(?,?,?,?,?,?)", (count, zdb, dbs, sigel, isil, ezb))
    c.execute("INSERT INTO web VALUES(?,?,?)", (count, homepage, opac))
    c.execute("INSERT INTO adress VALUES(?,?,?,?,?,?,?)", (count, street, city, zip, state,country, mail, phone))
    conn.commit()
    conn.close()

def drop_database():
    c, conn = connect_database()
    c.execute("DROP TABLE IF EXISTS sigil")
    conn.commit()
    conn.close()
write_database()