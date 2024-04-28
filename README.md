# Personal-Finance-Tracker-Using-Python

'''We define a Flask application with routes for adding expenses (/add_expense) and displaying all expenses (/).
The init_db() function initializes the SQLite database and creates a table called expenses to store expense records.
The /add_expense route handles POST requests to add a new expense to the database.
The / route fetches all expense records from the database and renders them using a Jinja2 template (index.html).
To run this code:

Save the code to a file named app.py.
Make sure you have Flask installed (pip install flask).
Run the Flask application by executing python app.py in your terminal.
Open your web browser and navigate to http://localhost:5000 to access the personal finance tracker.
You'll need to create the index.html template file in a templates folder within the same directory as app.py. This template will render the expense records fetched from the database.
'''




