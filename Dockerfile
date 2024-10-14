# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-dev

# Copy .env file into the container
COPY .env /app/.env

# Run app.py when the container launches
CMD ["poetry", "run", "python", "app.py"]
