FROM ubuntu:latest

# Install Python, pip, and system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy application code
COPY app.py .

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Install Flask (override PEP 668 restrictions)
RUN pip3 install --break-system-packages flask

# Expose Flask port
EXPOSE 5000

# Run Flask
CMD ["flask", "run", "--host=0.0.0.0"]
