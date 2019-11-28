echo wrk -t100 -c500 -d20s http://localhost:8080 ... asgi-100-500.log
wrk -t100 -c500 -d20s http://localhost:8080 > asgi-100-500.log
