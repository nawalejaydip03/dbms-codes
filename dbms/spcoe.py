import mysql.connector as c

con = c.connect(host='localhost',user='root',password='1234',database='spcoe')
cursor = con.cursor()

while True:
    n= input("Enter name :")
    a= int(input(" Enter Age:"))
    p= input ("Enter Address :")
    query="Insert into student values('{}',{},'{}')".format(n,a,p)
    cursor.execute(query)
    con.commit()
    print("Data inserted sucsessfully....")
    X=int(input( "1. Enter Entries\n 2. Exit"))
    if X == 2:
          break
