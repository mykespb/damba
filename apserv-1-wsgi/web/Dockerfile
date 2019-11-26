FROM python:3-slim-buster

LABEL MAINTAINER Mikhail Kolodin

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

ENTRYPOINT [ "python", "web.py" ]
CMD [ "python", "./web.py" ]
#ENTRYPOINT [ "start.sh" ]
#CMD [ "start.sh" ]
