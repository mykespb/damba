FROM python:3-slim-buster

LABEL MAINTAINER Mikhail Kolodin

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

#ENTRYPOINT [ "python", "script-bottle.py" ]
#CMD [ "python", "./script-bottle.py" ]
ENTRYPOINT [ "python", "script-quart.py" ]
CMD [ "python", "./script-quart.py" ]
