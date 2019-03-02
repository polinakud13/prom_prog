FROM python:3.4-alpine
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "/giver.py"]
COPY giver.py /giver.py
