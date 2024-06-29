from core.Query import DNSQuery

def setup_dns(option):
    
    if option == '+':
        name = input("Enter DNS name : ")
        primary_dns = input("Enter primary DNS : ")
        secondary_dns = input("Enter secondary DNS : ")
        try:
            DNSQuery().add_dns(name, primary_dns, secondary_dns)
            return {'success':True , 'code' : '200' , 'msg':'DNS added'}
        except:
            return {'success':False , 'code' : '400' , 'msg':'Something went wrong'}
    elif option == '-':
        dns_id = input("Enter DNS ID : ")
        try:
            if DNSQuery().delete_dns(dns_id) :
                return {'success':True , 'code' : '200' , 'msg':'DNS deleted successfully'}
            else:
                return {'success':False , 'code' : '400' , 'msg':'dns not found'}
        except:
            return {'success':False , 'code' : '400' , 'msg':'Something went wrong'}
    else:
        return {'success':False , 'code' : '400' , 'msg':'Invalid option'}