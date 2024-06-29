
import subprocess
import platform

def set_dns_option(option):
    if option == 1:
        primary_dns = '10.202.10.202'
        secondary_dns = '10.202.10.102'
    elif option == 2:
        primary_dns = '178.22.122.100'
        secondary_dns = '185.51.200.2'
    elif option == 3:
        primary_dns = '8.8.8.8'  # Google Public DNS servers
        secondary_dns = '8.8.4.4'
    else:
        raise ValueError('Invalid option selected')

    system = platform.system()
    if system == 'Windows':
        subprocess.run(['powershell', '-Command', f"Set-DnsClientServerAddress -InterfaceIndex (Get-NetAdapter).InterfaceIndex -ServerAddresses '{primary_dns}','{secondary_dns}'"])
        print(f"Primary DNS set to {primary_dns} and Secondary DNS set to {secondary_dns} for Windows.")
    elif system == 'Linux':
        result = subprocess.run(['uname', '-s'], capture_output=True, text=True)
        if result.stdout.strip() == 'Linux':
            subprocess.run(['nmcli', 'connection', 'modify', 'CONNECTION_NAME', f"ipv4.dns '{primary_dns},{secondary_dns}'"])
            subprocess.run(['nmcli', 'connection', 'modify', 'CONNECTION_NAME', 'ipv4.ignore-auto-dns', 'yes'])
            subprocess.run(['nmcli', 'connection', 'down', 'CONNECTION_NAME'])
            subprocess.run(['nmcli', 'connection', 'up', 'CONNECTION_NAME'])
            print(f"Primary DNS set to {primary_dns} and Secondary DNS set to {secondary_dns} for connection: CONNECTION_NAME")
    else:
        print("Unsupported operating system.")

def main():
    print("""
          1. 403
          2. shecan
          3. Google Public DNS servers""")
          
    option = int(input("Enter your option (1, 2, or 3): "))
    set_dns_option(option)

if __name__ == "__main__":
    main()
