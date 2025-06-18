# Kaylie Velazquez
# kjvelazquezbecerra@student.rtc.edu
# 05/29/2025
# Spring Qrt
# CNE 370: Introduction to Virtualization

# The following script will connect to Maxscale Instance and will be able to execute queries to display the following:
# Largest zipcodes in zipcode_one, all zipcodes in Kentucky, zipcodes between 40000-41000 and the TotalWage where state=PA

import mysql.connector

# connection to Maxscale connection
def connect_to_sql():
    conn = mysql.connector.connect(host='192.168.1.45', port=4000, user= "maxuser", password="maxpwd")

    return conn

con = connect_to_sql()
cursor = con.cursor()

# The largest zipcode in zipcode_one
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
print(cursor.fetchall())

# The largest zipcode in zipcode_two
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two ORDER BY Zipcode DESC LIMIT 1;")
print(cursor.fetchall())

# All zipcode where state=KY (Kentucky)
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one WHERE State='KY';")
print(cursor.fetchall())

# All zipcode where state=KY (Kentucky) in zipcodes_two
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two WHERE State='KY';")
print(cursor.fetchall())

# All zipcodes between 4000 and 41000
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 and 41000;")
print(cursor.fetchall())

# All zipcodes between 4000 and 41000 in zipcodes_two
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 and 41000;")
print(cursor.fetchall())

# The TotalWages column where state=PA (Pennsylvania)
cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state= 'PA';")
print(cursor.fetchall())

# The TotalWages column where state=PA (Pennsylvania) in zipcodes_two
cursor.execute("SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE state= 'PA';")
print(cursor.fetchall())

