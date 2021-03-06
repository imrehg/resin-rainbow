FROM resin/raspberrypi3-python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY rainbow.py ./

CMD python rainbow.py
