echo wrk -t10 -c10 -d20s http://localhost:8080 ... asgi-10-10.log
wrk -t10 -c10 -d20s http://localhost:8080 > asgi-10-10.log
