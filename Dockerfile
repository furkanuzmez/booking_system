# Use an official Python image as a base
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . .

# Set environment variables (optional, use .env for better management)
ENV PYTHONUNBUFFERED=1

# Run Django migrations and start the server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "booking_system.wsgi:application"]
