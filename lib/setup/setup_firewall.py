import subprocess

def configure_firewall(open_ports):
    try:
        # Block all ports
        subprocess.run(['sudo', 'ufw', 'default', 'deny'], check=True)
        
        # Allow specified ports
        for port in open_ports:
            subprocess.run(['sudo', 'ufw', 'allow', str(port)], check=True)
        
        # Enable UFW
        subprocess.run(['sudo', 'ufw', 'enable'], check=True)
        print("Firewall has been configured.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to configure firewall: {e}")


open_ports = [
    22, # SSH (for remote access)
    80, # HTTP (AdGuard)
    443, # HTTPS (AdGuard)
    53, # DNS (AdGuard)
    67, # DHCP (AdGuard)
    68, # DHCP (AdGuard)
    5443, 
    784 
]

configure_firewall(open_ports)