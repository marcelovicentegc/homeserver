import subprocess

def block_wifi():
    try:
        subprocess.run(['nmcli', 'radio', 'wifi', 'off'], check=True)
        print("WiFi has been blocked.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to block WiFi: {e}")