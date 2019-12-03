echo wrk -t100 -c500 -d20s http://localhost:8080 ... nginx-100-500.log
wrk -t100 -c500 -d20s http://localhost:8080 > nginx-100-500.log
