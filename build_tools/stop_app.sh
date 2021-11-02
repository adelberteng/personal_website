#!/bin/bash
_TOP_DIR_PATH=$(cd "$(dirname "$0")"; cd ..;pwd)
docker-compose -f $_TOP_DIR_PATH/docker/docker-compose.yaml down
