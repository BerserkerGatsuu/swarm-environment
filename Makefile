#!/bin/bash
IMAGE_NAME = berserkermirio/swarm-environment:rabbitmq
# Used to change the add all nodes as queue members
change_queues:
	@echo "Finding containers with image: $(IMAGE_NAME)"
	@if [ -n "$$(docker ps -q --filter ancestor=$(IMAGE_NAME))" ]; then \
		RANDOM_CONTAINER=$$(docker ps -q --filter ancestor=$(IMAGE_NAME) | shuf -n 1); \
		docker exec $$RANDOM_CONTAINER python3 /scaledown_scripts/change_queues.py; \
	else \
		echo "No containers found with this image: $(IMAGE_NAME)"; \
	fi

# Used after the change_queues command to scaledown the cluster and rebalance queues
scale_down:
	@echo "Finding containers with image: $(IMAGE_NAME)"
	@if [ -n "$$(docker ps -q --filter ancestor=$(IMAGE_NAME))" ]; then \
		RANDOM_CONTAINER=$$(docker ps -q --filter ancestor=$(IMAGE_NAME) | shuf -n 1); \
		docker exec $$RANDOM_CONTAINER python3 /scaledown_scripts/scaledown.py; \
		docker exec $$RANDOM_CONTAINER python3 /scaledown_scripts/rebalance_queues.py; \
		echo "hello"; \
	else \
		echo "No containers found with this image: $(IMAGE_NAME)"; \
	fi
			
