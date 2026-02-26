
Design pattern is nothing but the way of defining the rules of developing software applications.

Django follows MVT(Model View Template) Software Design Pattern.
1. Model is responsible for all database operations.
2. Template is basically front-end layout (HTML, Bootstrap)
3. View acts as a bridge between Model and Template. View is a function where the logic is written. Can't directly access the DB.


### Example: 
Users access Django application using urls(where we have the URL patterns listed). Matches the pattern and redirect to the corresponding function. The function contains the database queries. returns the response to model and then model sends the data to view. View then returns the response to the template to display the data.