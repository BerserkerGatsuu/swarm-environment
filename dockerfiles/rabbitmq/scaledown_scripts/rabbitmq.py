# Functions for scaling down rabbitmq cluster

import requests
import subprocess

# Function to get queue information
def get_queues(rabbitmq_api_url,username,password):
    queue_endpoint = rabbitmq_api_url + 'queues'
    response = requests.get(queue_endpoint, auth=(username, password))
    
    # Parse JSON 
    if response.status_code == 200:
        queues_info = response.json()
        queue_list = []

        # Save queues and info of them in a list
        for queue in queues_info:
            queue_info = {
                'name': queue['name'],
                'vhost': queue['vhost'],
                'type': queue['type']
            }
            if 'members' in queue:
                members = queue['members']
                queue_info['members'] = members if members else 'empty'               
            queue_list.append(queue_info)
        # Return the list with the queues info    
        return queue_list 
    else:
        print(f"Failed to fetch queue information. Status code: {response.status_code}")
        return None

# List of running rabbitmq nodes
def active_nodes():
    # Save cluster_status output in a variable
    CLUSTER_STATUS = subprocess.run(['rabbitmqctl', 'cluster_status', '--formatter','json'], capture_output=True, text=True).stdout

    # Use jq to manipulate the JSON data and find running nodes
    try:
        running_nodes = subprocess.run(['jq', '-r', '.running_nodes | join(" ")'], input=CLUSTER_STATUS, capture_output=True, text=True, check=True).stdout.strip().split()
    except subprocess.CalledProcessError as e:
        print(f"Error executing jq: {e}")
        exit(1)  
    # Return the nodes
    return running_nodes    

def non_cluster_members(members):
    running_nodes=active_nodes()
    # Check which running nodes are not members of a quorum queue
    non_members = [node for node in running_nodes if node not in members]
    # Return the nodes that are not members of a quorum queue
    return non_members

def non_running_nodes():
    running_nodes=active_nodes()
  #Save cluster_status output in a variable
    CLUSTER_STATUS = subprocess.run(['rabbitmqctl', 'cluster_status', '--formatter','json'], capture_output=True, text=True).stdout
   # Use jq to manipulate the JSON data and find disk nodes
    try:
        disk_nodes = subprocess.run(['jq', '-r', '.disk_nodes | join(" ")'], input=CLUSTER_STATUS, capture_output=True, text=True, check=True).stdout.strip().split()
    except subprocess.CalledProcessError as e:
        print(f"Error executing jq: {e}")
        exit(1)
    # Find and return the nodes not running (the disk nodes that are not running)
    nodes_not_running=list(set(disk_nodes)-set(running_nodes)) 
    return nodes_not_running
