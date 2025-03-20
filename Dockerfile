# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies (Django and other required packages)
RUN pip install --no-cache-dir django

# Expose the Django development server port
EXPOSE 8000

# Set the default command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
