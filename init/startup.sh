#!/bin/bash
unset LD_LIBRARY_PATH && \
    cd $HADOOP_CONF_DIR && \
    curl -O http://api.hdfs.marathon.l4lb.thisdcos.directory/v1/endpoints/core-site.xml && \
    curl -O http://api.hdfs.marathon.l4lb.thisdcos.directory/v1/endpoints/hdfs-site.xml && \
    cd - && \
    export LD_LIBRARY_PATH=/opt/mesosphere/libmesos-bundle/lib/
