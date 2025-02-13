import sqlite3

def create_database_table(db_name):
    """
    Creates a SQLite database and a table to store the CSV data.
    """
    connection = sqlite3.connect(db_name)  # Connect to the database (or create it if it doesn't exist)
    cursor = connection.cursor()

    # Create a table with columns: first_name, second_name, score
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            first_name TEXT,
            second_name TEXT,
            score INTEGER
        )
    ''')

    connection.commit()  # Commit the changes
    connection.close()  # Close the connection

def insert_data_into_db(db_name, people_data):
    """
    Inserts the parsed CSV data into the database table.
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Insert each person's data into the table
    for person in people_data:
        cursor.execute('''
            INSERT INTO scores (first_name, second_name, score)
            VALUES (?, ?, ?)
        ''', (person['First Name'], person['Second Name'], person['Score']))

    connection.commit()  # Commit the changes
    connection.close()  # Close the connection

def get_top_students(db_name):
    """
    Queries the database to find the top scorer(s).
    Returns a list of names and the top score.
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Find the highest score
    cursor.execute('SELECT MAX(score) FROM scores')
    highest_score = cursor.fetchone()[0]

    # Find all people with the highest score
    cursor.execute('''
        SELECT first_name, second_name
        FROM scores
        WHERE score = ?
        ORDER BY first_name, second_name
    ''', (highest_score,))

    top_scorers = cursor.fetchall()  # Fetch all top scorers
    connection.close()  # Close the connection

    # Format the names
    names = [f"{row[0]} {row[1]}" for row in top_scorers]
    return names, highest_score
