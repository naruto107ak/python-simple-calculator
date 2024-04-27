import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="anmol2006",database="dbsaloon")
cursor=con.cursor()
def insert():
    a=input("enter service name:")
    b=input("enter service cost:")
    
    query="insert into services(service_name,price)values('"+a+"','"+b+"');"
    print("record inserted successfully")
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def delete():
    a=input("enter service name:")
    query="delete from services where service_name='"+a+"';"
    print("record deleted successfully")
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def showdata():
    query="select * from services;"
    cursor.execute(query)
    record=cursor.fetchall()
    for i in record:
        print(i)
    con.commit()
    cursor.close()
    if con.is_connected:
        con.close()

def search():
    a=input("enter servicename:")
    query="select * from customers where service_name='"+a+"';"
    cursor.execute(query)
    record=cursor.fetchone()
    print(record)
    con.commit()
    cursor.close()
    con.close()





    