#This is a python app to count visits on a web page


FROM python:2.7-slim

MAINTAINER CondorLabs

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8080 available in Docker Network
EXPOSE 8080

# Define environment variable
ENV NAME CondorLabs

# Run app.py when the container launches
CMD ["python", "app.py"]
