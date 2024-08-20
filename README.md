# sys-o11y

This repository contains a set of industry standard services to monitor the system's health and performance. It is a good source for those who:
1. Are looking for a starting point to build their own monitoring stack.
2. Want to learn how to use Grafana, Prometheus and containerization.
3. Want to learn Rust.
4. Want to learn about micro-frontends.
5. Want to learn how to build multi-platform applications.

## Getting started

Once you've cloned the repository, you can start the services (on the background) with the following command:

```bash
docker compose up -d
```

| Service       | URL                     | Description               |
| ------------- | ----------------------- | ------------------------- |
| Grafana       | http://localhost:32911/ | Visualize the data        |
| Prometheus    | http://localhost:52441/ | Collect and store metrics |
| Portainer     | http://localhost:37017/ | Manage Docker containers  |
| Node Exporter | -                       | Monitor the host machine  |
| cAdvisor      | -                       | Monitor Docker containers |


## Configuration

The services are configured to monitor the host machine, including the Docker containers and Prometheus itself. You have to manually configure Prometheus as a data source in Grafana and check the targets in Prometheus to make sure everything is working as expected.

The JSON configuration of each dashboard is stored in the [grafana/dashboards](./grafana/dashboards/) directory. You can import them in Grafana to visualize the data.

## Building the desktop application

As this project extends to a desktop application to visualize all services available through a single page, abstracting the random IPs assigned to each of them, you can use the following command to spin a Tauri application that points to each of the services through a WebView:

```bash
cd frontend
pnpm install
pnpm tauri android init

# For Desktop development, run:
pnpm tauri dev

# For Android development, run:
pnpm tauri android dev
```

> Muke sure to have all required dependencies installed: cargo, Node.js and system dependencies required by Tauri.

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

### Grabbing a random available port.

You may want to add another service to the stack. You can use the following command to get a random available port to use:

```bash
python3 ./scripts/get_random_available_port.py
```
