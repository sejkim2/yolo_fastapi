# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Install system dependencies including libGL and libglib2.0-0 (no need for libgthread-2.0-0)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install OpenCV dependencies
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY conf/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install OpenCV version that is compatible with your code
RUN pip install opencv-python-headless==4.5.3.56

# Copy the application code
COPY app/ /app/

# Copy the weights (models)
COPY weights/ /app/weights/

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
