# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files to the container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Set environment variables (optional but good)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app using Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
