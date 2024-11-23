import subprocess

def what_is_my_ip_to_the_world():
    try:
        subprocess.run(['curl', 'ifconfig.me'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get IP address: {e}")

def what_is_my_ip_in_lan():
    try:
        subprocess.run(['hostname', '-I'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get IP address: {e}")