from rabbitmq import get_queues , non_cluster_members
import subprocess
import os

# RabbitMQ server credentials and url
rabbitmq_api_url = 'http://nginx:15672/api/'
username = os.environ.get('RABBITMQ_DEFAULT_USER')
password = os.environ.get('RABBITMQ_DEFAULT_PASS')

data=get_queues(rabbitmq_api_url,username,password)
# Iterate through each object in the JSON array
index = 1
for queue_info in data:
    name = queue_info["name"]
    vhost = queue_info["vhost"]
    type = queue_info["type"]

# Check if queue type is quorum or not
    if type != "quorum":
      print('queue '+name+' is not quorum')
      continue;
      
    members = queue_info["members"] # members/replicas of a queue
    non_members=non_cluster_members(members) # nodes that are not members of a queue

# Check if the queue has all the running nodes as members or not
    if not non_members:
        print("All nodes are members in queue ",name)
        continue;

    # Loop through the members array for each queue
    for non_member in non_members:
        #print("Adding member to queue : "+name+" in vhost : "+vhost)
        subprocess.run(["rabbitmq-queues", "add_member", "--vhost", vhost, name, non_member])        

    index += 1