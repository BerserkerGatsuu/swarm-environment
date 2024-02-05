#FROM rabbitmq:3.7.8-management
FROM rabbitmq:3-management

RUN apt-get update -y && \
    apt-get install -y jq

RUN apt-get install -y python3-pip && \
    pip3 install requests

COPY rabbitmq.conf /etc/rabbitmq
COPY scaledown_scripts /scaledown_scripts
RUN rabbitmq-plugins enable --offline rabbitmq_peer_discovery_consul