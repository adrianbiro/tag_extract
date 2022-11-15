FROM python:3.10-slim

COPY requirements.txt .
copy extract.py .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "extract.py"]
