import os
import subprocess
from get_login_info import host, user

# Define the remote machine details
remote_path = f"/home/{user}/Documents/homeserver"

def fresh_copy_to_remote():
    os.chdir("./deploy")
    subprocess.run(["scp", "-r", ".", f"{user}@{host}:{remote_path}"], check=True)

# Only run this upon initial setup
fresh_copy_to_remote()
