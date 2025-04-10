import mysql.connector

mydb = mysql.connector. connect (
    host="localhost",
    user="root",
    password="root",
)

mycursor= mydb.cursor()

# Create the database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

mydb.database = "mydatabase"

mycursor.execute("""CREATE TABLE IF NOT EXISTS user(
                 id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                 name VARCHAR(255),
                 age INT,
                 address VARCHAR(255))""")



data =[
    ('Paula', 28,'Valley Road')
    ('Alice', 21, 'USIU LKB Building')
    ('BOB', 22, 'Kasarani mall')
    ('Matt', 25, 'Muthaiga Towers')
    ('Zippy', 30, 'Nairobi Town')
]


mycursor.executemany("INSERT INTO user (name, age, address) VALUES (%s, %s, %s)", data)

mydb.commit()

sqlusers = "SELECT * FROM user"
mycursor.execute(sqlusers)

myresult = mycursor.fetchall()

for user in myresult:
    print(user)



