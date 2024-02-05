from rabbitmq import non_running_nodes
import subprocess

non_running_nodes=non_running_nodes()
if not non_running_nodes:
    print("No nodes are down")
# Remove the nodes that are down from the cluster
for node in non_running_nodes:
    subprocess.run(["rabbitmqctl","forget_cluster_node",node])