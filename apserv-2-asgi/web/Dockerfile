FROM python:3-slim-buster

LABEL MAINTAINER Mikhail Kolodin

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

#ENTRYPOINT [ "python", "web.py" ]
#CMD [ "python", "./web.py" ]
#ENTRYPOINT [ "hypercorn",  "web:app", "-b", "0.0.0.0:80", "--keep-alive", "1000" ]
#CMD [ "hypercorn",  "web:app", "-b", "0.0.0.0:80", "--keep-alive", "1000" ]

ENTRYPOINT [ "./start.sh" ]
#CMD [ "./start.sh" ]
