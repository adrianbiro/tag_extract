FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
copy extract.py .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "/app/extract.py"]
