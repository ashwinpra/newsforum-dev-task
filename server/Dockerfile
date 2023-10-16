# Use the official Python image as the base image
FROM python:3.11

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Create and set the working directory for the application
WORKDIR /app

# Copy the Flask backend source code and database file
COPY . /app

RUN source venv/bin/activate

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port for the Flask backend
EXPOSE 5000

# Start the Flask backend
CMD ["flask", "run"]