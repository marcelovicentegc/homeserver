import os
import subprocess
from env.get_login_info import host, user
from spin_services import spin_services

# Define the remote machine details
remote_path = f"/home/{user}/Documents/homeserver"

def copy_updates_to_remote():
    result = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True, check=True)
    print(result.stdout)
    changed_files = result.stdout.splitlines()
    for file in changed_files:
        if file.startswith("deploy/"):
            os.chdir("./deploy")
            file = file.replace("deploy/", "")
            subprocess.run(["scp", file, f"{user}@{host}:{remote_path}/{file}"], check=True)

copy_updates_to_remote()
