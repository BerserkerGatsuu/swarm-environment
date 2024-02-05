FROM openjdk:8-jre-slim

# jupyterlab install and run

ARG shared_workspace=/opt/workspace
ARG pyspark_version=3.5.0
ARG jupyterlab_version=2.1.5

RUN mkdir -p ${shared_workspace} && \
    apt-get update -y && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

ENV SHARED_WORKSPACE=${shared_workspace}

VOLUME ${shared_workspace}

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install wget pyspark==${pyspark_version} jupyterlab==${jupyterlab_version}

RUN pip3 install boto3 && \
    pip3 install pika

# -- Runtime

EXPOSE 8888
WORKDIR ${SHARED_WORKSPACE}
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=