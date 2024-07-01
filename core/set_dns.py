import subprocess
import platform
import ctypes
import os

from core.Query import DNSQuery


def is_admin():
    try:
        if platform.system() == "Windows":
            return ctypes.windll.shell32.IsUserAnAdmin()
        else:
            return os.geteuid() == 0
    except:
        return False

def get_linux_interface():
    try:
        result = subprocess.run(['ip', '-o', '-4', 'route', 'show', 'to', 'default'], capture_output=True, text=True)
        interface = result.stdout.split()[4]
        return interface
    except:
        return None
    
def install_network_manager():
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'network-manager'], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing NetworkManager:: {e}")
        return False

def get_connection_name():
    try:
        result = subprocess.run(['nmcli', '-t', '-f', 'NAME', 'connection', 'show'], capture_output=True, text=True)
        connections = result.stdout.strip().split('\n')
        # برگرداندن اولین اتصال موجود
        return connections[0] if connections else None
    except:
        return None

def set_dns_option(option):
    if not is_admin():
        return {'success': False, 'code': '500', 'msg': "The application is NOT running with administrative privileges."}

    if option != 0:
        try:
            dns = DNSQuery().get_id(option)
            primary_dns = dns.primary_dns
            secondary_dns = dns.secondary_dns
        except:
            return {'success': False, 'code': '400', 'msg': 'Invalid DNS selected'}

    system = platform.system()
    if system == 'Windows':
        if option == 0:
            subprocess.run(['powershell', '-Command', 'Set-DnsClientServerAddress "*" -ResetServerAddresses'])
            return {'success': True, 'msg': "DNS servers reset for Windows."}
        else:
            subprocess.run(['powershell', '-Command', f"Set-DnsClientServerAddress -InterfaceIndex (Get-NetAdapter).InterfaceIndex -ServerAddresses '{primary_dns}','{secondary_dns}'"])
            return {'success': True, 'msg': f"Primary DNS set to {primary_dns} and Secondary DNS set to {secondary_dns} for Windows."}
    elif system == 'Linux':
        try:
            subprocess.run(['nmcli', '-v'], check=True)
        except FileNotFoundError:
            if not install_network_manager():
                return {'success': False, 'code': '500', 'msg': "NetworkManager  - not installed."}
        connection_name  = get_connection_name()
        if not connection_name:
            return {'success': False, 'code': '500', 'msg': "Network connection not found."}
        
        if option == 0:
            subprocess.run(['nmcli', 'con', 'mod', connection_name , 'ipv4.ignore-auto-dns', 'no'])
            subprocess.run(['nmcli', 'con', 'mod', connection_name , 'ipv4.dns', ''])
            subprocess.run(['nmcli', 'con', 'up', connection_name ])
            return {'success': True, 'msg': "DNS servers reset for Linux."}
        else:
            # dns_addresses = f"{primary_dns} {secondary_dns}" #"10.1.1.1 1.1.1.1"
            subprocess.run(['nmcli', 'con', 'mod', connection_name , 'ipv4.dns', primary_dns])
            subprocess.run(['nmcli', 'con', 'mod', connection_name, '+ipv4.dns', secondary_dns])
            subprocess.run(['nmcli', 'con', 'mod', connection_name , 'ipv4.ignore-auto-dns', 'yes'])
            subprocess.run(['nmcli', 'con', 'up', connection_name ])
            return {'success': True, 'msg': f"Primary DNS set to {primary_dns} and Secondary DNS set to {secondary_dns} for Linux."}
    else:
        return {'success': False, 'code': '500', 'msg': "Unsupported operating system."}
