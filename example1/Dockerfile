# Use an official Python runtime as a parent image
FROM python:3.13-slim
#creates a directory called app and sets it as the working directory
WORKDIR /app
#copies the contents of the current directory on the host machine to the /app directory in the container
COPY . /app
#installs the dependencies specified in the requirements.txt file using pip
RUN pip install -r requirements.txt
# Describe that the container will listen to port 80
EXPOSE 80
#Defines an environment variable called name with the value furko
ENV name=furko
#Specifies the command to run when the container starts, which is to execute the app.py file using python3
CMD ["python3", "app.py"]