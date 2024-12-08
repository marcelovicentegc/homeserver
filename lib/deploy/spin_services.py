from __future__ import print_function, unicode_literals
import subprocess
from env.get_login_info import host, user

# Define the remote machine details
remote_path = f"/home/{user}/Documents/homeserver"

def spin_services():
    ssh_process = subprocess.Popen(['ssh',
                                '-tt'
                                f"{user}@{host}:{remote_path}"],
                                stdin=subprocess.PIPE, 
                                stdout = subprocess.PIPE,
                                universal_newlines=True,
                                bufsize=0)
    ssh_process.stdin.write("docker compose up -d\n")
    ssh_process.stdin.write("echo END\n")
    ssh_process.stdin.write("uptime\n")
    ssh_process.stdin.write("logout\n")
    ssh_process.stdin.close()


    for line in ssh_process.stdout:
        if line == "END\n":
            break
        print(line,end="")

    #to catch the lines up to logout
    for line in  ssh_process.stdout: 
        print(line,end="")

