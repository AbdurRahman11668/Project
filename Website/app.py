from flask import Flask, render_template, session, render_template, request, g, jsonify
import sqlite3
import random
import os

app = Flask(__name__)

# SQLite connection function
# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect('Videogames.db')
#     return db

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of app.py
DATABASE = os.path.join(BASE_DIR, '..', 'Videogames.db')  # Go one level up to find database.db


# Function to connect to the database
def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row 
    return connection

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html', 
                           data_source="Source of your data (e.g., a public dataset)",
                           variables={"Column1": "Description 1", "Column2": "Description 2"})

# Route for the Data page
# @app.route('/data')
# def data():
#     conn = get_db()
#     cursor = conn.execute('SELECT * FROM VideoGameStocks')
#     rows = cursor.fetchall()
#     conn.close()
#     return render_template('data.html', rows=rows)

@app.route('/data')
def data():
    try:
        conn = get_db()
        cursor = conn.execute('SELECT * FROM VideoGameStocks LIMIT 20')
        rows = cursor.fetchall()
        print(rows)  # Debug: check if rows contain data
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        rows = []  # Fallback to an empty list if there's an error
    finally:
        conn.close()
    return render_template('data.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)

