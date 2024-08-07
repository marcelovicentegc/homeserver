# sys-o11y

## Getting started

Once you've cloned the repository:

```bash
docker compose up -d
```

| Service    | URL                     |
| ---------- | ----------------------- |
| Grafana    | http://localhost:32911/ |
| Prometheus | http://localhost:52441/ |
| Portainer  | http://localhost:37017/ |

## Useful debug commands

```bash
# What is my machine's IP address within my LAN?
ip -c a

# What is the state of the Prometheus' targets?
open http://localhost:52441/targets
```
