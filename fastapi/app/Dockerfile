FROM python:3.9

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python3", "main.py"]
