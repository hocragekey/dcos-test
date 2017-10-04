FROM mesosphere/spark:2.0.1-2.2.0-1-hadoop-2.6

#Pulling the HDFS files from the local hdfs instance on the DCOS cluster
#This will work the default hdfs service name
#This is all thanks to Susan X. Huynh!
COPY conf /etc/hadoop

COPY py /code/
