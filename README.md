# DJANGO-REST-API
**Restful api developed with django-rest framework which 
gets consumed by react application in the frontend.**

# Install the command line client
$ pip install coreapi-cli

# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action api list

EXAMPLE:-
# Load the schema document
$ coreapi get http://127.0.0.1:8000/docs/

# Interact with the API endpoint
$ coreapi action api create -p category=... -p title=... -p slug=... -p author=... -p excerpt=... -p content=... -p status=...