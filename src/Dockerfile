FROM python:3.12-alpine3.20
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py /app
CMD ["python", "main.py"]
