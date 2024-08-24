# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /home/jasper/apt_sim/environments

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the main APT simulation script
CMD ["python", "main.py"]
