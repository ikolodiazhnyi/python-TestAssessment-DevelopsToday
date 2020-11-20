News board API
====================

START
------------

- Clone the repository
	> git clone https://github.com/ikolodiazhnyi/python-TestAssessment-DevelopsToday.git
- Open the project with any IDE
- Move on the same level with manage.py file
- Install Django, Rest Framework
	> pip install django
	
	> pip install djangorestframework
- Run server
	> python3 manage.py runserver

ENDPOINTS
--------------

- http://127.0.0.1:8000/api/posts/ :
    > Send a `GET` request to get a list of all existing posts in the database
	> Send a `POST` request to create a post


- http://127.0.0.1:8000/api/posts/<int:pk>/ :
    > Send a `GET` request to get a particular post from the database
    
    > Send a ‘PUT’ request to update a particular post
    
    > Send a ‘PATCH’ request to update a particular field in the certain post
    
    > Send a ‘DELETE’ request to delete a particular post


- http://127.0.0.1:8000/api/comments/ :
    > Send a `GET` request to get a list of all existing comments in the database
    
    > Send a `POST` request to create a comment


- http://127.0.0.1:8000/api/comments/<int:pk>/ :
    > Send a `GET` request to get a particular comment from the database
    
    > Send a ‘PUT’ request to update a particular comment
    
    > Send a ‘PATCH’ request to update a particular field in the certain comment
    
    > Send a ‘DELETE’ request to delete a particular comment


- http://127.0.0.1:8000/api/upvotes/<int:pk> :
	> Send a ‘PATCH’ request to increase a particular post’s amount_of_upvotes field by 1


- http://127.0.0.1:8000/admin/ :
	> Open an admin page


- http://127.0.0.1:8000/api/
	> Send a `GET` request to get a list of existing urls
