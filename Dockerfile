FROM python:3.8.5

# Set application working directory
WORKDIR /usr/src/

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install application
COPY . .

# Run application




#CMD gunicorn -c config/gunicorn.py application:app
