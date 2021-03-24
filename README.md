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

The first set of business was to set up the flask up which first needs a virtual enviroment. In order to set up the virtual enviroment, I had to do 'python -m venv venv' which is already built into python. The reason we want to set up a virtual enviroment is to place all our packages only in this enviroment so in the future, these packages aren't installed globabaly which can intefer with other programs. Flask if the first package we have to install which is very similar to running a node server. When Flask runs, it will try to call a function create_app() so we had to create a create_app() and define it in the '__init__.py' file in the app directory which will call any static resources from the root directory. In this same '__init__.py" file in the app directory is where we will be calling our routes, initiating our database connection and using Jinja to fill out some of our pages.




The next step is create models for our database so when a user posts information or login, that data is collected and stored. The first thing that is needed is to create some models. It is best to open a new git branch and have that branch only deal with the models so everything is isolated. It also prevents any mistakes being done on the main branch. In our terminal, run 'mysql -u root -p' to run mysql and create the database name you want for this project which I did called python_news_db; This will hold the other tables which will contain the information. After creating the table, make sure the virtual enviroment takes place and make sure that sqlalchemy, pymsqsl and python-dotenv is installed.It is very important that in the .env you will need to create host this 'DB_URL=mysql+pymysql://root:<password>@localhost/python_news_db' connection. It be best to make a db directory and place a schema.sql to drop and create the database.

 *it is important to notice that any directory with a __init__.py makes that directoy a package and the files in that directory a module which makes things easier to export/import.
    



## Contributors
Michael Bartek


## Contact
Hoybaby

If you have any questions, contact the author directly at mbartek436@gmail.com.
