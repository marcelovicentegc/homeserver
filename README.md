# sys-o11y <!-- omit in toc -->

This repository contains a set of industry standard services to monitor the system's health and performance. It is a good source for those who:
1. Are looking for a starting point to build their own monitoring stack.
2. Want to learn how to use Grafana, Prometheus and containerization.

- [Getting started](#getting-started)
- [Configuration](#configuration)
- [Debugging](#debugging)
  - [Moving the server to a different LAN](#moving-the-server-to-a-different-lan)
  - [Grabbing a random available port](#grabbing-a-random-available-port)

## Getting started

Once you've cloned the repository, you can start the services (on the background) with the following command:

```bash
docker compose up -d
```

| Service       | URL                     | Description                                                  |
| ------------- | ----------------------- | ------------------------------------------------------------ |
| Homepage      | http://localhost:3000/  | Access the desktop app with shortcuts for all services below |
| Grafana       | http://localhost:32911/ | Visualize the data                                           |
| Prometheus    | http://localhost:52441/ | Collect and store metrics                                    |
| Portainer     | http://localhost:37017/ | Manage Docker containers                                     |
| Node Exporter | -                       | Monitor the host machine                                     |
| cAdvisor      | -                       | Monitor Docker containers                                    |


## Configuration

The services are configured to monitor the host machine, including the Docker containers and Prometheus itself. You have to manually configure Prometheus as a data source in Grafana and check the targets in Prometheus to make sure everything is working as expected.

The JSON configuration of each dashboard is stored in the [grafana/dashboards](./grafana/dashboards/) directory. You can import them in Grafana to visualize the data.

## Debugging

### Moving the server to a different LAN

If moving the server to another LAN, you may need to change the IP address of the Prometheus' targets OR Grafana datasources. You can use the following commands to help you with that:

```bash
# What is my machine's IP address within my LAN?
ip -c a
```

```bash
# What is the state of the Prometheus' targets?
open http://localhost:52441/targets
```

### Grabbing a random available port

You may want to add another service to the stack. You can use the following command to get a random available port to use:

```bash
python3 ./scripts/get_random_available_port.py
```
