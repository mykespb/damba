echo wrk -t50 -c50 -d20s http://localhost:8080 ... nginx-50-50.log
wrk -t50 -c50 -d20s http://localhost:8080 > nginx-10-50.log
