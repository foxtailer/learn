FROM python:3.11.9-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# RUN pip install --upgrade pip

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# When navigate to project folder and run: docker build -t image_name:tag .
# Copy files from curent(project) dir to /app dir in container
COPY . .

# Execute after container start
CMD ["python", "counter.py"]