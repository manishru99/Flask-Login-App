# Step 1: Setting up the Dockerfile for the project

# Use the official Python 3.9 image
FROM python:3.9-slim
# Set environment variables to prevent Python from writing .pyc files and to ensure output is flushed immediately
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the locale to UTF-8 to handle Unicode characters properly
ENV LANG C.UTF-8
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install the dependencies specified in requirements.txt
RUN pip install -r requirements.txt
# Expose port 3000 for the Flask app
EXPOSE 3000
# Command to run the Flask application
CMD python ./app.py