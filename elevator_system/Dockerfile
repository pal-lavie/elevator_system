FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /elevator_system

# Set the working directory to /music_service
WORKDIR /elevator_system

# Copy the current directory contents into the container at /music_service
ADD . /elevator_system/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8080
