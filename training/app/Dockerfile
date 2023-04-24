# Set the base image to Python 3.8
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY training.py  ./

# Copia il file requirements.txt all'interno della directory di lavoro
COPY requirements.txt ./

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the command to train the model
CMD ["python", "training.py"]