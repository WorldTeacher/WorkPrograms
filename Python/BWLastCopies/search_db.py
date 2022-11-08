import sqlite3


def connect_database():
    """
    This function will connect to the database.

    Returns:
        c : The cursor.
        conn: The connection.
    """
    conn = sqlite3.connect('sigil.db')
    c = conn.cursor()
    return c, conn

def search_sigil(sigil: str)->str:
    """
    This function will search for the given sigil in the database.

    Args:
        sigil (str): The sigil to be searched for.

    Returns:
        result (str): The id of the sigil.
    """
    c, conn = connect_database()
    c.execute("SELECT id FROM sigil WHERE isil=?", (sigil,))
    data = c.fetchone()
    conn.close()
    result=data[0] #result is a tuple, so we need to get the first element
    return result
def search_data(id:str)->dict[str,str]:
    """
    This function will search for the given id in the database.

    Args:
        id (str): The id to be searched for.

    Returns:
        result: A dict with the data extracted from the database.
            
    """
    c, conn = connect_database()
    result={'adress':[], 'phone':[], 'mail':[], 'homepage':[],'name':[],'isil_link':[]}
    c.execute("SELECT street,city, zip_code,state FROM adress WHERE id=?", (id,))
    data = c.fetchone()
    for elem in data:
        result['adress'].append(elem)
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
    """
    This function will search for the given sigil in the database.\n
    Args:
        sigil (str): The sigil to be searched for.\n
    Returns:
        result (dict): A dict with the data extracted from the database.
            Data:
                adress (str): The adress of the library.
                phone (str): The phone number of the library.
                email (str): The email of the library.
                homepage (str): The homepage of the library.
                name (str): The name of the library.
                isil_link (str): The link to the isil homepage of the library.
    """
    id=search_sigil(sigil)
    result=search_data(id)
    return result
