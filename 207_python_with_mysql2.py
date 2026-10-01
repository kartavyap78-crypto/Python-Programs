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

Roll_No = int(input("enter a roll no = "))
Name = input("enter a name = ")
English = int(input("enter a eng marks = "))
Maths = int(input("enter a maths marks = "))
Science = int(input("enter a sci marks = "))
Total = int(input("enter a total marks"))
Percentage = int(input("ente a percentage = "))
Grade = input("enter a grade = ")
query = f"insert into Student Values({Roll_No},'{Name}',{English},{Maths},{Science},{Total},{Percentage},'{Grade}')"
# Fetch data from Student table
cur.execute(query)
con.commit()

print("Record Inserted Successfully")

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