import os
import subprocess
from get_login_info import host, user

# Define the remote machine details
remote_path = f"/home/{user}/Documents/homeserver"

def copy_updates_to_remote():
    os.chdir("./deploy")
    result = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True, check=True)
    print(result.stdout)
    changed_files = result.stdout.splitlines()
    for file in changed_files:

        if file.startswith("deploy/"):
            subprocess.run(["scp", file, f"{user}@{host}:{remote_path}/{file}"], check=True)

copy_updates_to_remote()
