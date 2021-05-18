# flask-CRUD-app
An app to keep track of items while I move house.

virtualenv venv
source activate/bin/source
pip install -r requirement.txt
python app/app.py

# wsgi 
wsgi.py is the entrypoint
python wsgi.py

use the server of your choice.

# guincorn
seve with gunicorn
gunicorn -c config/gunicorn.py wsgi:app

Listens on port 5105. Settings in config/gunicorn.py

# Containerized

Build on docker and run anywhere, no installation required!

```docker build -t "dushyant/item-tracker" ``` \
```docker run -p 5105:5105 "dushyant/item-tracker```
