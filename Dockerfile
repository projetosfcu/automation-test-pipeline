# Use official Python image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

RUN pip install flask
# Run unit tests
RUN python test_app.py

CMD ["python", "app.py"]
