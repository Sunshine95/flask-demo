# flask-CRUD-app
An app to keep track of items while I move house.

# wsgi 
wsgi.py entrypoint
eg. seve with gunicorn
gunicorn -c config/gunicorn.py wsgi:app

# Containerized
docker build -t "image/name"
docker run --network=host "image/name"
