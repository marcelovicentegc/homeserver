import os
import subprocess
from get_login_info import host, user

# Define the remote machine details
remote_path = f"/home/{user}/Documents/homeserver"

def spin_services():
    subprocess.run(["ssh", f"{user}@{host}:{remote_path}", "docker compose up -d"], check=True)

spin_services()