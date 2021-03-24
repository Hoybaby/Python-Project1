#Python Newsfeed

## Description
This application is for users/individuals to share websites that may be able to help individuals gain more knowledge in a speific area. More knowledge means more power. This website can help bring more insight to certain areas of Programming or Tech in general. 

## Table of Contents

* [Installation](#installation)

* [Usage](#usage)

* [License](#license)

* [Tests](#tests)

* [Process](#process)

* [Contributors](#contributors)

* [Contact](#contact)


## Installation
Packages required to run this program are: Need to make sure to have python installed and to set up a virtual enviroment to install the necessary packages. The packages that need to be installed are flask, sqlalchemy, pymysql, python-dotenv, bcrypt, and  cryptography. To install these packages, the indivudal has to type the command 'pip install' and packages I used.


## Deployable Link
Link to live program: https://python-news-feed.herokuapp.com/


## License
The license that is being used is MIT. Can be found in the license folder.


## Tests
To test, run the following command: To run the program, make sure you are in the virtual enviroment by running .\venv\Scripts\activate then running the command py -m flask run.

## Process
 


 *It is important to notice that any directory with a '__init__.py' makes that directoy a package and the files in that directory a module which makes things easier to export/import.
    

The first set of business was to set up the flask up which first needs a virtual enviroment. In order to set up the virtual enviroment, I had to do 'python -m venv venv' which is already built into python. The reason we want to set up a virtual enviroment is to place all our packages only in this enviroment so in the future, these packages aren't installed globabaly which can intefer with other programs. Flask if the first package we have to install which is very similar to running a node server. When Flask runs, it will try to call a function create_app() so we had to create a create_app() and define it in the '__init__.py' file in the app directory which will call any static resources from the root directory. In this same '__init__.py" file in the app directory is where we will be calling our routes, initiating our database connection and using Jinja to fill out some of our pages.


Setting Up Database connection:
The next step is create models for our database so when a user posts information or login, that data is collected and stored. The first thing that is needed is to create some models. It is best to open a new git branch and have that branch only deal with the models so everything is isolated. It also prevents any mistakes being done on the main branch. In our terminal, run 'mysql -u root -p' to run mysql and create the database name you want for this project which I did called python_news_db; This will hold the other tables which will contain the information. After creating the table, make sure the virtual enviroment takes place and make sure that sqlalchemy, pymsqsl and python-dotenv is installed.It is very important that in the .env you to reference the database in this way :'DB_URL=mysql+pymysql://root:<password>@localhost/python_news_db' connection. It be best to make a db directory and place a schema.sql to drop and create the database. In the 'db/__init__.py', it is a must to create three variable to connect to the database using env variable.



Finalizing homepage:

When the database is all done, the next big piece of work is to finialize the homepage and populate it with sample information. In the previous sectio, we need more setup to prepare it for Flask. In order to do so, we had to add a litle more code in the 'app/db/__init__.py' which will be 'Base.metadata.create_all() method'. We have the then import this function into the 'app/__init__.py and place this function inside the 'create_app()' function. To finish prepping the db package we need to define another function that returns a session. Whenever this function is called, it returns a new session-connection object. Other modules in the app can import Session directly from the db package, but using a function means that we can perform additional logic before creating the database connection. Once the connection is done and models are define, we implement them in the routes. It is IMPORTANT to close the connecto to database when we are done because it can cause the app to crash in production.  To do this, we create a close_db() function to handle it when we are done.



Login Session:

For user logins, we need to create api endpoints which will be done when we make an api.py in the routes directory. In this directory, we will be placing routes to guide users when they log in and check if their log in is correct. For routing in Pyton, using Blueprint,request and jsonify from Flask and using the decorator @bp.route is very important. Whenever a route is made, make sure that you import that route into the 'app/__init__.py' and register that route in the 'create_app() function in the root __init__.py. These routes will POST the information that is being retrieved from the front end into the models that we made for the MySql database as shown in 'routes/api.py'. When we store these input values into another variable that uses the Python Dictionary(JavaScript Property equivalent) system, we have to commit these information into the database with a db.add(variable). However, it is important to remember that the db.add only ques that information to be put in and doesn't insert into the database. It needs db.commit() to execute the query. 





## Contributors
Michael Bartek


## Contact
Hoybaby

If you have any questions, contact the author directly at mbartek436@gmail.com.
