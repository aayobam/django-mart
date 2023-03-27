FROM python-3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working director
WORKDIR /django-mart

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project code
COPY . /jango-mart/

# Expose the port
EXPOSE 8000

# Run the command
RUN ["python", "manage.py", "runserver", "0.0.0.0:8000"]
