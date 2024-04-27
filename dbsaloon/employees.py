import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="anmol2006",database="dbsaloon")
cursor=con.cursor()
def insert():
    a=input("enter employee name:")
    b=input("enter your address:")
    c=input("enter your phone number:")
    query="insert into employees(employee_name,address,phone_no)values('"+a+"','"+b+"','"+c+"');"
    print("record inserted successfully")
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def delete():
    a=input("enter employeename:")
    query="delete from employees where employee_name='"+a+"';"
    print("record deleted successfully")
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def showdata():
    query="select * from employees;"
    cursor.execute(query)
    record=cursor.fetchall()
    for i in record:
        print(i )
    con.commit()
    cursor.close()
    if con.is_connected:
        con.close()

def search():
    a=input("enter employee name:")
    query="select * from employees where employee_name='"+a+"';"
    cursor.execute(query)
    record=cursor.fetchone()
    print(record)
    con.commit()
    cursor.close()
    con.close()




    