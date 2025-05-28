import mysql.connector

username = input("Enter your username: ")
password = input("Enter your password: ")

# WARNING: This is vulnerable to SQL injection
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"

db = mysql.connector.connect(
    user='root',
    password='root',
    host='127.0.0.1',
    port=6603,
    database='dbe'
)
cursor = db.cursor()
cursor.execute(query)
result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

db.close()
