 ## Flask Application Design

### HTML Files

**1. index.html**
- This is the main HTML file that will serve as the user interface for the application.
- It will contain the necessary HTML elements to display the rate comparison form and the results.

**2. form.html**
- This HTML file will contain the form elements for the user to input the rate data.
- It will include fields for hourly rate, level, location, and supplier.

**3. results.html**
- This HTML file will display the results of the rate comparison.
- It will show the comparison of hourly rates for the same level and location, as well as the total of mixed rates and locations from across multiple suppliers.

### Routes

**1. @app.route('/')**
- This route will handle the main page of the application.
- It will render the index.html file.

**2. @app.route('/form')**
- This route will handle the form submission.
- It will collect the user input from the form and store it in a database.
- It will then redirect the user to the results page.

**3. @app.route('/results')**
- This route will handle the display of the results.
- It will retrieve the rate data from the database and perform the necessary calculations.
- It will then render the results.html file with the comparison results.