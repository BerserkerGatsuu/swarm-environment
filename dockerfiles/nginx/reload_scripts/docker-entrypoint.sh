#!/bin/bash
###########

sh -c "nginxReloader.sh &"
exec /docker-entrypoint.sh "$@"