import subprocess
import platform
import ctypes
from core.Querys import DNSQuery







def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

if not is_admin():
    print("The application is NOT running with administrative privileges.")

def set_dns_option(option):
    if option == 0:
        primary_dns = ''
        secondary_dns = ''
    else:
        try:
            DNSQuery.get_id(option)
        except:
            print("Invalid option.")
            return False

    system = platform.system()
    if system == 'Windows':
        


            
        if option == 4:
            subprocess.run(['powershell', '-Command', 'Set-DnsClientServerAddress "*" -ResetServerAddresses'])
            print("DNS servers reset for Windows.")
        else:
            subprocess.run(['powershell', '-Command', f"Set-DnsClientServerAddress -InterfaceIndex (Get-NetAdapter).InterfaceIndex -ServerAddresses '{primary_dns}','{secondary_dns}'"])
            print(f"Primary DNS set to {primary_dns} and Secondary DNS set to {secondary_dns} for Windows.")
    # elif system == 'Linux':
    #     if option == 4:
    #         subprocess.run(['nmcli', 'connection', 'modify', 'CONNECTION_NAME', 'ipv4.dns', '""'])
    #         subprocess.run(['nmcli', 'connection', 'modify', 'CONNECTION_NAME', 'ipv4.ignore-auto-dns', 'no'])
    #         subprocess.run(['nmcli', 'connection', 'down', 'CONNECTION_NAME'])
    #         subprocess.run(['nmcli', 'connection', 'up', 'CONNECTION_NAME'])
    #         print("DNS servers reset for Linux.")
    #     else:
    #         result = subprocess.run(['uname', '-s'], capture_output=True, text=True)
    #         if result.stdout.strip() == 'Linux':
    #             subprocess.run(['nmcli', 'connection', 'modify', 'CONNECTION_NAME', f"ipv4.dns '{primary_dns},{secondary_dns}'"])
    #             subprocess.run(['nmcli', 'connection', 'modify', 'CONNECTION_NAME', 'ipv4.ignore-auto-dns', 'yes'])
    #             subprocess.run(['nmcli', 'connection', 'down', 'CONNECTION_NAME'])
    #             subprocess.run(['nmcli', 'connection', 'up', 'CONNECTION_NAME'])
    #             print(f"Primary DNS set to {primary_dns} and Secondary DNS set to {secondary_dns} for connection: CONNECTION_NAME")
    else:
        print("Unsupported operating system.")

def main():
    print("""DNS changer by parsa momtazi nejad
          1. 403
          2. shecan
          3. Google Public DNS servers
          0. Reset DNS servers""")
          
    option = int(input("Enter your option (1, 2, 3, or 0): "))
    set_dns_option(option)

if __name__ == "__main__":
    main()
