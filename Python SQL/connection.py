import mysql.connector

# establising the connection
conn = mysql.connector.connect(
  user="root",
  password="",
  host="127.0.0.1",
  database="pythonsql"
)

# creating cursor object
cursor = conn.cursor()

# Executinh query
cursor.execute("SELECT DATABASE()")

# Fetch a single row using fetchone() method
data = cursor.fetchone()

print('Connection Established to', data)


# closing the connection
conn.close()