import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="anmol2006",database="dbsaloon")
cursor=con.cursor()
def insert():
    a=input("enter username:")
    b=input("enter your address:")
    c=input("enter your password:")
    query="insert into users(user_name,address,password)values('"+a+"','"+b+"','"+c+"');"
    print("record inserted successfully")
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def delete():
    a=input("enter username:")
    c=input("enter your password:")
    query="delete from users where user_name='"+a+"' and password='"+c+"' ;"
    print("record deleted successfully")
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def showdata():
    query="select * from users;"
    cursor.execute(query)
    record=cursor.fetchall()
    for i in record:
        print(i )
    con.commit()
    cursor.close()
    if con.is_connected:
        con.close()
def search():
    a=input("enter username:")
    query="select * from users where user_name='"+a+"';"
    cursor.execute(query)
    record=cursor.fetchone()
    print(record)
    con.commit()
    cursor.close()
    con.close()






    