from flask import Flask, render_template, session, render_template, request, g, jsonify
import sqlite3
import os
import credentials

app = Flask(__name__)



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, '..', 'Videogames.db') 



# Function to connect to the database
def get_db():
    try:
        connection = sqlite3.connect(DATABASE)
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None


@app.route('/')
def home():
    return render_template('home.html', 
                           data_source="Source of your data (e.g., a public dataset)",
                           variables={"Column1": "Description 1", "Column2": "Description 2"})

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html', 
                           data_source="Source of your data (e.g., a public dataset)",
                           variables={"Column1": "Description 1", "Column2": "Description 2"})


@app.route('/data')
def data():
    try:
        conn = get_db()
        cursor = conn.execute('SELECT * FROM VideoGameStocks')
        rows = cursor.fetchall()
        print(rows)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        rows = [] 
    finally:
        conn.close()
    return render_template('data.html', rows=rows)

# api-key route

@app.route('/weather')
def weather():
    api_key = credentials.weather_api_key
    return f"Your Weather API Key is: {api_key}"


if __name__ == '__main__':
    app.run(debug=True)

