FROM python:3.10.10

WORKDIR /berry-api

ADD requirements.txt .
ADD ./templates ./templates
ADD ./src ./src 

RUN pip install -r requirements.txt

CMD ["python", "src/app.py"]