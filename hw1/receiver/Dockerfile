 FROM python:3.4-alpine
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "/receiver.py"]
COPY receiver.py /receiver.py
