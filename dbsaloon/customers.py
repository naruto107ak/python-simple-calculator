import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="anmol2006",database="dbsaloon")
cursor=con.cursor()
def insert():
    a=input("enter name:")
    b=input("enter your address:")
    c=input("enter your phone number:")
    query="insert into customers(customer_name,address,phone_no)values('"+a+"','"+b+"','"+c+"');"
    print("record inserted successfully")
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def delete():
    a=input("enter name:")
    query="delete from users where user_name='"+a+"';"
    print("record deleted successfully")
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def showdata():
    query="select * from customers;"
    cursor.execute(query)
    record=cursor.fetchall()
    for i in record:
        print(i )
    con.commit()
    cursor.close()
    if con.is_connected:
        con.close()

def search():
    a=input("enter customername:")
    query="select * from customers where customer_name='"+a+"';"
    cursor.execute(query)
    record=cursor.fetchone()
    print(record)
    con.commit()
    cursor.close()
    con.close()





    