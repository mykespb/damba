FROM python:3

LABEL MAINTAINER Mikhail Kolodin

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT [ "python", "script.py" ]
CMD [ "python", "./script.py" ]

