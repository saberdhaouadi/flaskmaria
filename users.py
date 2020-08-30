import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="saber123",
        database="saberdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM MyUsers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
