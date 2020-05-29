# MindMatchDP
 
# Versiunea functionala e ultimul commit de pe branch-ul development sau master
 
Run: & pip install -r requirements.txt

This will set up the databases used by django:

	& python manage.py makemigrations

	$ python manage.py migrate

If you get any kind of errors at makemigrations or migrate run:

	$ python manage.py migrate --run-syncdb

Start the server:

	& python manage.py runserver

The urls are:
	localhost:8000/profile - accepts get request and returns json with all user profiles
	localhost:8000/profile/new/ - accepts post request to add a new profile
	localhost:8000/profile/<int:pk>/ (eq. /profile/1) - accept get request and returns a single profile
	localhost:8000/cnp - accepts get request and returns all cnp's
	localhost:8000/cnp/new/ - accepts post request and adds a new cnp
	localhost:8000/cnp/<int:pk>/ - accepts get request and returns cnp for one single user
	localhost:8000/question - accepts get request and returns all the questions with their answers
	localhost:8000/question/<int:pk>/ - accepts get request and returns one question with it's answer
	localhost:8000/match/<int:pk>/ - accepts get request and returns the mathcing user profiles in the compatibility order

pentru a adauga intrebari in backend, run:
	$ python manage.py createsuperuser
	create a user for you
	& python manage.py runserver
	http://127.0.0.1:8000/admin -> add question

Access the link: ' http://127.0.0.1:8000/  '

On the upper-right part you have Login and Register:

try to register with a new account

	- login

	- once login you can see profile and logout on the upper-right side

	- you can logout and login as many times as you want

	- you can access the following url: ' http://127.0.0.1:8000/admin '

	- than you can login with the username: 'admin' and the password 'avaelgo'

	- once entered in the admin page you can see all registered users and their data
	- you can also add data 
