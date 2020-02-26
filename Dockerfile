FROM python:3.8-alpine
LABEL maintainer="Kizzii <apisit.kizzii@gmail.com>"

WORKDIR /var/www/html

RUN apk update && apk add musl-dev gcc libffi-dev libressl-dev bash

COPY requirements.txt /var/www/html

RUN pip3 install -r requirements.txt

COPY . /var/www/html

RUN chmod +x entrypoint.sh

EXPOSE 80

ENTRYPOINT ["./entrypoint.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:80", "--log-level", "debug", "wsgi:app"]
