# Use official Ubuntu image as base
FROM ubuntu:latest

# Install Python
RUN apt update && apt install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy necessary files
COPY scientific_calculator.py test_scientific_calculator.py /app/

# Set entrypoint command to run tests
ENTRYPOINT ["python3", "/app/scientific_calculator.py"]

