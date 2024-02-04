# swarm-environment
A containerized environment for Docker Swarm.


You can deploy a containerized environment using Docker Swarm.
You should go to the directory that contains this compose file and start initialize Swarm. After that deploy the stack with the command:
                              docker stack deploy -c <compose-file> <stack_name>
and the containerized environment after a few minutes will be ready for use. This environment is mostly used to collect data from APIs, send the to MinIO Object Storage, use Jupyterlab with Apache Spark to create a spark session and analyze the data collected. Lastly, we use RabbitMQ to transmite the analyzed data. We can also scale up or down the RabbitMQ cluster.                             
