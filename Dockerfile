FROM python:3.6


WORKDIR /app

COPY requirements.txt .

ENV FLASK_APP=app.py

RUN pip install -r requirements.txt

COPY . .
COPY run2.sh
RUN chmod a+x run2.sh

EXPOSE 5000

CMD ["./run2.sh"]
