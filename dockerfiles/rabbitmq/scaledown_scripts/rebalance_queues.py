from rabbitmq import get_queues , non_cluster_members , active_nodes
import subprocess
import random
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

    # Check if queue is quorum or not
    if type != "quorum":
      print('Queue '+name+' is not a quorum queue.Going to the next queue in line.')
      continue;

    members = queue_info["members"] # members/replicas
    running_nodes=active_nodes() # running nodes 
    non_members=non_cluster_members(members) # nodes that are not members 

    if len(members) < 3:
    # Add members if needed (members lower than 3)
      print("Queue "+name+" does not have enough members.Choosing random running node to add as member...")
      while len(members) <= 3:
        random_node = random.choice(running_nodes) # choose a random running node 
        print(random_node)
        # If its not a member add the node as a member else go choose another node
        if random_node not in members: 
          subprocess.run(["rabbitmq-queues", "add_member", "--vhost", vhost, name, random_node])
          members.append(random_node)
        else:
          print("Node "+random_node+" is member of the queue "+name)
    else: 
      # select 3 random members of a queue and remove all the other members
      random_members = random.sample(members,3)
      other_nodes = [node for node in members if node not in random_members]
      if not other_nodes:
        print("No members need to be removed from 'queue': "+name+" 'vhost': "+vhost)  
      for nodes in other_nodes:
        subprocess.run(["rabbitmq-queues", "delete_member", "--vhost", vhost, name, nodes])
      
    index += 1  