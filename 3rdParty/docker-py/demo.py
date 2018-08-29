#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import docker

if __name__ == '__main__':
    client = docker.from_env()
    # show images
    # 
    images = client.images()
    containers = client.containers()
    sw = client.swarm()
