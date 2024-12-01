# Project

# Project Group 5: Evaluation of VideoGame Share

### Description of the project
Its purpose is to allow stock data analysis of the videogaming industry: a web application affording a way to connect to a SQLite database for storage and actions upon stock data. Thus, it was responsive and meant to exhibit, in front, the SMO commands to the database in order to run multiple queries and show individual stock's history.

### Features
Web Interface: Created in Flask for maximum user activity.
Database Management: Efficient manipulation of data via SQLite for storing and retrieving.
Importing and exporting data: Able to import stock data from CSV files.
Dynamic analysis: Those stocks can be queried historically filtered by date, company, and ticker symbol.

### How to run the project
1. Install the necessary Python libraries using the requirements.txt file:
    * pip install -r requirements.txt

2. Set up database: Run the Jupyter scripts provided to either initialize the SQLite database (Videogames.db) or populate it.
3. Web App Initialization: Start the Flask app and run the server. In your browser: 
    * python app.py

4. Use the application: Use the webinterface to analyze, query, and visualize stock data.

### Description of Files
* Project_Group-5.ipynb: Java script in Jupyter Notebook for database creation, data analysis, and CSV handling..
* requirements.txt: Dependencies necessary for running the project. 
* README.md: The immediate document describing the project in a broader sense.  

### Prerequisite
* Python 3.7 and above
* SQLite installed on your computer

### Acknowledgements
This project is the result of the effort of Group 5. It is in a way a collaborative effort in the various aspects of database handling, web development, and data analysis.