# sys-o11y

## /etc/services

1. Open your favorite code editor:
```bash
code /etc/services
```

2. Add the following lines to the file to make them accessible with friendly names:
```txt
grafana       32911/tcp
prometheus    52441/tcp
portainer     37017/tcp
```

Reference: https://unix.stackexchange.com/questions/611406/how-to-assign-a-friendly-name-to-a-port-number-in-linux