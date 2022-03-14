### To build the image just run:
docker build -t cluster-apache-spark:3.0.2 .

### The final step to create your test cluster will be to run the compose file:
docker-compose up -d


### To validate your cluster just access the spark UI on each worker & master URL

Spark Master: http://localhost:9090
Spark Worker 1: http://localhost:9091
Spark Worker 2: http://localhost:9092


### To check database server
psql -U postgres -h 0.0.0.0 -p 5432
password is 'password' (set in docker-compoose.yml)

On terminal run 
1. psql -U postgres -h 0.0.0.0 -p 5432 (password: password)
2. CREATE DATABASE testgdc;

### To submit spark application

/opt/spark/bin/spark-submit --master spark://spark-master:7077 \
--jars /opt/spark-apps/postgresql-42.2.22.jar \
--driver-memory 1G \
--executor-memory 1G \
/path-to-testgendeconfiance/main.py