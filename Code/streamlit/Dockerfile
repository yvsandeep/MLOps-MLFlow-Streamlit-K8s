# Use the official Python base image
FROM python:3.8

# Set a directory for the app
WORKDIR /usr/src/app

# Install required Python modules
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the app files to the container
COPY . .

# Expose the port the app runs on
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py"]

