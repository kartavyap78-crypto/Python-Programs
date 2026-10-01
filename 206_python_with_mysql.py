import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # Agar password hai to yaha likho
    database="dbgls"
)

# Cursor create
cur = con.cursor()

# Fetch data from Student table
cur.execute("SELECT * FROM Student")

# Print all records
data = cur.fetchall()

for row in data:
    print(row)

# Close connection
cur.close()
con.close()