echo wrk -t100 -c100 -d20s http://localhost:8080 ... nginx-100-100.log
wrk -t100 -c100 -d20s http://localhost:8080 > nginx-100-100.log
