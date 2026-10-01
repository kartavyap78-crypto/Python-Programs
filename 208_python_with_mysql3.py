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

Roll_no = int(input("enter a roll no = "))
query = f"delete from student where Roll_No = {Roll_no}"
# Fetch data from Student table
cur.execute(query)
con.commit()

# print("Record Inserted Successfully")

# Display all records
cur.execute("SELECT * FROM Student")
# Print all records
data = cur.fetchall()


for row in data:
    # Roll_No,Name,English,Maths,Science,Total,Percentage,Grade = row
    # print(Roll_No,Name,English,Maths,Science,Total,Percentage,Grade)
    # Name = row
    print(row)
    

# Close connection
cur.close()
con.close()