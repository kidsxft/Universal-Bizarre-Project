import sqlite3
from datetime import datetime

# Connect to Database - Establishes connection, and will create it if not detected.
def create_database_connection():
    try:
        conn = sqlite3.connect('data.db')
        return conn
    except sqlite3.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

# Creating Table - Creates the table in our database
def create_table():
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS data (
                username VARCHAR(255) NOT NULL PRIMARY KEY,
                password VARCHAR(255) NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                stand VARCHAR(255) NOT NULL,
                money INT NOT NULL,
                rokaFruit INT NOT NULL,
                arrow INT NOT NULL,
                steelBall INT NOT NULL,
                frog INT NOT NULL,
                tommyGun INT NOT NULL,
                sword INT NOT NULL,
                stoneMask INT NOT NULL,
                redAja INT NOT NULL,
                requiemArrow INT NOT NULL,
                rebirthArrow INT NOT NULL,
                ajaMask INT NOT NULL,
                diary INT NOT NULL,
                bone INT NOT NULL,
                corpsePart INT NOT NULL,
                fruit INT NOT NULL,
                disc INT NOT NULL
            )
        ''')
        conn.commit()
        cursor.close()
    except sqlite3.Error as err:
        print(f"Error creating data table: {err}")

# Executing SQL Queries - Executes queries and returns results
def execute_query(query, params=None):
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        results = cursor.fetchall()
        cursor.close()
        return results
    except sqlite3.Error as err:
        print(f"Error executing query: {err}")
        return []

# Dealing with functions - Create, Read, Update, Delete
# Create - Creates with a New Title and Body
def create_login(username='', password=''):
    insert_query = "INSERT INTO data (username, password, stand, money, rokaFruit, arrow, steelBall, frog, tommyGun, sword, stoneMask, redAja, requiemArrow, rebirthArrow, ajaMask, diary, bone, corpsePart, fruit, disc) VALUES (?, ?, 'None', 250, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)"
    params = (username, password)
    execute_query(insert_query, params)
    print("login created successfully.")

# Read - Retrieves login by its ID
def get_login(username):
    select_query = "SELECT password FROM data WHERE username = ?"
    params = (username,)
    results = execute_query(select_query, params)
    results = [t[0] for t in results]
    if len(results) == 1:
        print(f"Retrieved login {username} successfully.")
        result = results[0]
    else:
        print(f"login {username} not found.")
        result = None
    return result

# Getting List of all data - Ordered in Update Time
def get_all_data():
    select_query = "SELECT * FROM data ORDER BY created_at DESC"
    results = execute_query(select_query)
    print(f"Retrieved {len(results)} login(s) successfully.")
    return results

# Finds user's specific data
def getData(varName, username):
    query = f"SELECT {varName} FROM data WHERE username = ?"
    params = (username,)
    results = execute_query(query, params)
    results = [t[0] for t in results]
    return results

# Update user's data
def updateData(varName, valUsed, username):
    query = f"UPDATE data SET {varName} = '{valUsed}' WHERE username = ?"
    params = (username,)
    results = execute_query(query, params)
    return results

# Getting List of all data - Ordered in Update Time
def get_all_usernames():
    select_query = "SELECT username FROM data ORDER BY created_at DESC"
    results = execute_query(select_query)
    results = [t[0] for t in results]
    print(f"Retrieved {len(results)} username(s) successfully.")
    return results

# Update - Updates a login with a New Title and Body
def update_login(username, variable, new_password):
    update_query = f"UPDATE data SET {variable} = ?, WHERE username = ?"
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    params = (variable, new_password, now, username)
    execute_query(update_query, params)
    print(f"Updated login {username} successfully.")

# Delete - Permanently Deletes data from the DB
def delete_login(username):
    delete_query = "DELETE FROM data WHERE username = ?"
    params = (username,)
    execute_query(delete_query, params)
    print(f"Deleted login {username} successfully.")
