import sqlite3


def connect_database():
    conn = sqlite3.connect('sigil.db')
    c = conn.cursor()
    return c, conn

def search_sigil(sigil: str)->str:
    c, conn = connect_database()
    c.execute("SELECT id FROM sigil WHERE isil=?", (sigil,))
    data = c.fetchone()
    conn.close()
    #result is in a tuple, so we need to get the first element
    return data[0]
def search_data(id):
    c, conn = connect_database()
    result={'adress':[], 'phone':[], 'mail':[], 'homepage':[],'name':[],'isil_link':[]}
    c.execute("SELECT street,city, zip_code,state FROM adress WHERE id=?", (id,))
    data = c.fetchone()
    for elem in data:
        result['adress'].append(elem)
    # result['adress']=data[0],data[1],data[2],data[3]
    c.execute("SELECT contact_phone, contact_mail FROM contact WHERE id=?", (id,))
    c_data = c.fetchone()
    result['phone']=c_data[0]
    result['mail']=c_data[1]
    c.execute("SELECT homepage,isil_page FROM web WHERE id=?", (id,))
    w_data = c.fetchone()
    result['homepage']=w_data[0]
    result['isil_link']=w_data[1]
    c.execute("SELECT name FROM data WHERE id=?", (id,))
    d_data = c.fetchone()
    result['name']=d_data[0]
    return result

def search_database(sigil: str)->dict:
    id=search_sigil(sigil)
    result=search_data(id)
    return result
