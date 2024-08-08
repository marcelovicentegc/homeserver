# sys-o11y

This repository contains a set of industry standard services to monitor the system's health and performance. It is a good source for those who:
1. Are looking for a starting point to build their own monitoring stack.
2. Want to learn how to use Grafana, Prometheus and Portainer.
3. Want to learn how to use Tauri to build desktop applications using Rust.

## Getting started

Once you've cloned the repository, you can start the services (on the background) with the following command:

```bash
docker compose up -d
```

| Service    | URL                     |
| ---------- | ----------------------- |
| Grafana    | http://localhost:32911/ |
| Prometheus | http://localhost:52441/ |
| Portainer  | http://localhost:37017/ |

To visualize all of them on a single page, you can use the following command to spin a Tauri application pointing to the URLs above through a WebView (you have to muke sure to have all dependencies installed, including cargo, Node.js and system dependencies):

```bash
cd frontend && cargo tauri dev
```

## Useful debug commands

```bash
# What is my machine's IP address within my LAN?
ip -c a

# What is the state of the Prometheus' targets?
open http://localhost:52441/targets
```
