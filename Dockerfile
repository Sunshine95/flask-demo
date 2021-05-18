FROM python:3.8.5

# Set application working directory
WORKDIR /usr/src/item-tracker-flask

# Install requirements
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install application
COPY . .

# Run application
EXPOSE 5105
CMD gunicorn -c config/gunicorn.py wsgi:app
