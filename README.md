# homeserver <!-- omit in toc -->

This repository contains the code that runs on my homeserver.

- [Getting started](#getting-started)
- [Configuration](#configuration)
- [Operating homeserver](#operating-homeserver)
  - [Moving the server to a different LAN](#moving-the-server-to-a-different-lan)
  - [Grabbing a random available port](#grabbing-a-random-available-port)
  - [Checking which application is running on a specific port](#checking-which-application-is-running-on-a-specific-port)

## Getting started

Once you've cloned the repository, you can start the services (on the background) with the following command:

```bash
docker compose up -d
```

| Service       | URL                    | Description                                                  |
| ------------- | ---------------------- | ------------------------------------------------------------ |
| Homepage      | http://localhost:3000/ | Access the desktop app with shortcuts for all services below |
| Grafana       | -                      | Visualize the data                                           |
| Prometheus    | -                      | Collect and store metrics                                    |
| Portainer     | -                      | Manage Docker containers                                     |
| Node Exporter | -                      | Monitor the host machine                                     |
| Dozzle        | -                      | Monitor Docker logs                                          |
| AdguardHome   | -                      | DNS and DHCP Server                                          |

## Configuration

The services are configured to monitor the host machine, including the Docker containers and Prometheus itself. You have to manually configure Prometheus as a data source in Grafana and check the targets in Prometheus to make sure everything is working as expected.

The JSON configuration of each dashboard is stored in the [grafana/dashboards](./grafana/dashboards/) directory. You can import them in Grafana to visualize the data.

## Operating homeserver

Below are some useful commands to help you operate (debug, fix, add new features, etc.) the homeserver.

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

### Checking which application is running on a specific port

You can use the following command to check which application is running on a specific port:

```bash
lsof -i :3000
```
