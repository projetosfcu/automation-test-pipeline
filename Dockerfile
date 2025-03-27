# Use official Python image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy app files
COPY app.py test_app.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Run unit tests
RUN python -m unittest test_app.py

CMD ["python", "app.py"]
