import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'abcd1234'
)

#prepare cursor object

cursorObject = dataBase.cursor()

#create db
cursorObject.execute("CREATE DATABASE restaurantcrmdb")

print("All done")