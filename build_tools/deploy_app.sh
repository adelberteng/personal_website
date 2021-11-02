#!/bin/bash
_TOP_DIR_PATH=$(cd "$(dirname "$0")"; cd ..;pwd)
# python3 ./src/secret_to_config.py
docker-compose -f $_TOP_DIR_PATH/docker/docker-compose.yaml up -d
