import subprocess

def who_is_using_this_port(port):
    try:
        subprocess.run(['lsof', '-i', f':{port}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to check who is using port {port}: {e}")

# who_is_using_this_port(22)