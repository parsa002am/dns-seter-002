import subprocess
import platform
import ctypes

from core.Query import DNSQuery


def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

def set_dns_option(option):
    if not is_admin():
        return {'success':False , 'code' : '500' , 'msg':"The application is NOT running with administrative privileges."}

    if(option != 0):
        try:
            dns = DNSQuery().get_id(option)
            primary_dns= dns.primary_dns
            secondary_dns = dns.secondary_dns
        except:
            return {'success':False , 'code' : '400' , 'msg':'Invalid DNS selected'}
    
    system = platform.system()
    if system == 'Windows':   
        if option == 0:
            subprocess.run(['powershell', '-Command', 'Set-DnsClientServerAddress "*" -ResetServerAddresses'])
            return {'success':True , 'msg':"DNS servers reset for Windows."}
        else:
            subprocess.run(['powershell', '-Command', f"Set-DnsClientServerAddress -InterfaceIndex (Get-NetAdapter).InterfaceIndex -ServerAddresses '{primary_dns}','{secondary_dns}'"])
            return {'success':True , 'msg':f"Primary DNS set to {primary_dns} and Secondary DNS set to {secondary_dns} for Windows."}
            
    
    else:
        return {'success':False , 'code' : '500' , 'msg':"Unsupported operating system."}