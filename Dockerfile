# Use a base Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app
RUN pip install pylint pytest

# Copy the rest of the application code
COPY . .

# Default command (can be overridden in the Jenkinsfile)
CMD ["pytest"]
