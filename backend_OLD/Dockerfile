FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /app/data

COPY . .

# Add the current directory to PYTHONPATH
ENV PYTHONPATH=/app

# Change to src directory and run the application
WORKDIR /app/src
CMD ["python", "main.py"]