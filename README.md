# homeserver <!-- omit in toc -->

This repository contains the code that runs on my homeserver.

- [Getting started](#getting-started)
- [Configuration](#configuration)

## Getting started

Once you've cloned the repository, you can start the services with the following command:

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

The services are configured to monitor the host machine and Prometheus itself. You have to manually configure Prometheus as a data source in Grafana and check the targets in Prometheus to make sure everything is working as expected.