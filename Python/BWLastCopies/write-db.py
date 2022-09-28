
import sqlite3
from time import sleep
import json5 as json
import glob
from termcolor import colored
'''jsonfile="C:/Users/aky547/GitHub/isil/data/DE-Bs32.json"
json_count=glob.glob("C:/Users/aky547/GitHub/isil/data/*.json")
count=0
for file in json_count:
    count=count+1
    #print(file, count)'''
def extract_data(jsonfile):
    fields={'001A','001B','001D','001U','002@','003@','008H','009Q','029@','029A','032P','035B','035E','035I','047A','035G','035Q','035P','035D','035L','035O','029R','035H','035J','035K','007N','035M','035N'}
    return_data = {'zdb': None, 'dbs': None, 'sigel': None, 'isil': None, 'ezb': None, 'homepage': None, 'add_link': None, 'street': None, 'city': None, 'country': None, 'zip': None, 'state': None, 'shortname': None, 'longname': None, 'orgatype': None, 'phone': None, 'mail': None, 'isil_link': None, 'message':None, 'name':None}
    
    with open(jsonfile, "r", encoding="utf-8") as f:
        data = json.load(f)
    zdb, dbs, sigel, isil, ezb, homepage, opac, street, city, country, zip, state, shortname, longname, orgatype,phone, mail = "","","","","","","","","","","","","","","","",""
    phone_city=""
    phone_country=""
    phone_number=""
    message=""
    metadata=data['data']
    for field in metadata:
        if field in fields:
            if field == '008H':
                adressdata=metadata[field][0]
                for entry in adressdata:
                    for key in entry:
                        if key == 'a': 
                            zdb=entry[key]
                            return_data['zdb'] = zdb
                        if key == 'b':
                            dbs=entry[key]
                            return_data['dbs'] = dbs
                        if key == 'd':
                            sigel=entry[key]
                            return_data['sigel'] = sigel
                        if key == 'e':
                            isil=entry[key]
                            return_data['isil'] = isil
                        if key == 'f':
                            ezb=entry[key]
                            return_data['ezb'] = ezb
                            
            if field =='009Q':
                    for content in metadata[field]:
                        temp_dict = {k:v for subdict in content for k, v in subdict.items()} 
                        if temp_dict.get("z", None) == 'A':
                            homepage=temp_dict.get("u", None)
                            return_data['homepage'] = homepage
                        if temp_dict.get("z", None) == 'B':
                            opac=temp_dict.get("u", None)
                            return_data['add_link'] = opac
            if field =='029@':
                namedata=metadata[field][0]
                for entry in namedata:
                    for key in entry:
                        if key =='a':
                            shortname=entry[key]
                            return_data['shortname'] = shortname
            if field =='029A':
                namedata=metadata[field][0]
                for entry in namedata:
                    for key in entry:
                        if key =='a':
                            longname=entry[key]
                            return_data['longname'] = longname
            if field == '032P':
                sigildata=metadata[field][0]
                for entry in sigildata:
                    #entries are like this {'a': 'Kunzenweg 21'}
                    # based on identifier, get value
                    for key in entry:
                        if key == 'a':
                            street=entry[key]
                            return_data['street'] = street
                        if key == 'b':
                            city=entry[key]
                            return_data['city'] = city
                        if key == 'd':
                            country=entry[key]
                            return_data['country'] = country
                        if key == 'e':
                            zip=entry[key]
                            return_data['zip'] = zip
                        if key == 'f':
                            state=entry[key]
                            return_data['state'] = state
            if field == '035B':
                maildata=metadata[field][0]
                for entry in maildata:
                    for key in entry:
                        if key == 'd':
                            phone_country=entry[key]

                        if key=='e':
                            phone_city=entry[key]
                        if key=='f':
                            phone_number=entry[key]
            
           
                        #if keys d, e, f  exist, create phone number
                        
                            
                        if key == 'k':
                            mail=entry[key]
                            return_data['mail'] = mail
            if field=='047A':
                message=metadata[field][0][0]['a']
                return_data['message'] = message
                '''if phone_country and phone_city and phone_number != None:
                            phone=f'+{phone_country} {phone_city}{phone_number}'
                    else:
                        phone=None'''
                    
                
            
                
            if field == '035E':
                typedata=metadata[field][0]
                for entry in typedata:
                    for key in entry:
                        if key == 'f':
                            orgatype=entry[key]
                            return_data['orgatype'] = orgatype
    isil_link=data['sameAs'][0:]
    name=data['name']
    return_data['name'] = name
    return_data['isil_link'] = isil_link
    #print(phone, mail)   
    if phone_country and phone_city and phone_number != None:
        phone=f'+{phone_country} {phone_city}{phone_number}'
    else:
        phone=None
    return_data['phone'] = phone
    #print(zdb, dbs, sigel, isil, ezb, homepage, opac, street, city, country, zip, state, shortname, longname, orgatype,phone, mail)     
    return return_data
def connect_database():
    conn = sqlite3.connect('sigil.db')
    c = conn.cursor()
    return c, conn
def list_tables():
    c, conn = connect_database()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(c.fetchall())
def write_database(data):
    c, conn = connect_database()
    
    zdb=data['zdb']
    dbs=data['dbs']
    sigel=data['sigel']
    isil=data['isil']
    ezb=data['ezb']
    homepage=data['homepage']
    opac=data['add_link']
    street=data['street']
    city=data['city']
    country=data['country']
    zip=data['zip']
    state=data['state']
    shortname=data['shortname']
    longname=data['longname']
    name=data['name']
    orgatype=data['orgatype']
    phone=data['phone']
    mail=data['mail']
    isil_link=data['isil_link']
    message=data['message']
    print(data)
    idlist=[]
    
    c, conn = connect_database()
    id=generate_id()
    if id in idlist:
        generate_id()
    else:
        idlist.append(id)
        
    #insert data into database if not already present
    #c.execute("INSERT OR IGNORE INTO sigil (zdb, dbs, sigel, isil, ezb, homepage, opac, street, city, country, zip, state, shortname, longname, orgatype, phone, mail) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (zdb, dbs, sigel, isil, ezb, homepage, opac, street, city, country, zip, state, shortname, longname, orgatype, phone, mail))
    c.execute("INSERT INTO  data (id, shortname, longname,name,type)VALUES(?,?,?,?,?)", (id,shortname,longname,name,orgatype))
    c.execute("INSERT INTO adress (id,street, city, zip_code, state, country) VALUES(?,?,?,?,?,?)", (id,street,city,zip,state,country))
    c.execute("INSERT INTO contact (id,contact_mail, contact_phone) VALUES(?,?,?)", (id,mail,phone))
    c.execute("INSERT INTO sigil (id,zdb, dbs, sigil, isil, ezb) VALUES(?,?,?,?,?,?)", (id,zdb,dbs,sigel,isil,ezb))
    c.execute("INSERT INTO web (id,homepage, add_link,isil_page) VALUES(?,?,?,?)", (id,homepage,opac,isil_link))
    if message != None:
        c.execute("INSERT INTO information (information,id) VALUES(?,?)", (message,id))
    #c.execute("INSERT INTO information (information) VALUES(?)", (message))
    conn.commit()
    conn.close()

def drop_database():
    c, conn = connect_database()
    c.execute("DROP TABLE IF EXISTS sigil")
    conn.commit()
    conn.close()

def generate_id():
    import random
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers='0123456789'
    #generate random id using numbers and letters, check if id already exists in database
    
    id = ''.join(random.choice(letters) for i in range(8))
    id += ''.join(random.choice(numbers) for i in range(8))
    id=scramble(id)
    return id

def scramble(self):
    import random
    list=[]
    for i in self:
        list.append(i)
    random.shuffle(list)
    return ''.join(list)

jsonfiles = glob.glob("C:/Users/aky547/GitHub/isil/data/*.json")

for file in jsonfiles:
    print(colored(file, 'magenta' ,on_color='on_white', attrs=['bold']))
    write_database(extract_data(file))
    #sleep(0.1)
    #write_database(file)
#list_tables()
#print(extract_data(jsonfiles[6940]))
'''print(generate_id())'''
#print(extract_data("C:/Users/aky547/GitHub/isil/data/AT-FHJ-G.json"))