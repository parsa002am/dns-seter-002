from config import *
from core.Query import DNSQuery
from core.set_dns import set_dns_option
from core.setup_dns import setup_dns








def main():

    while True:
        print("DNS changer by parsa momtazi nejad (parsa002am)")
        dnss = DNSQuery().get_all_dns()
        for dns in dnss:
            print(f"{dns.id}. {dns.name} ")
        print("0. Reset DNS servers")
        print("----------------------------------------------------------------")
        print('+. add DNS server')
        print('-. remove DNS server')

            
        option = input("Enter your option : ")
        if option.isnumeric():
            try:
                result = set_dns_option(int(option))
            except Exception as e:
                result = {'success':False , 'code' : '400' , 'msg':f'Something went wrong:{e}'}
            if result['success'] is True:
                print(result['msg'])
            else :
                if result['code'] == 400 :
                    print(result['msg'])
                    print('please try again!')
                    continue
                elif result['code'] == 500:
                    input(result['msg'])
                    exit(1)
        else :
            try:
                result = setup_dns(option)
            except Exception as e:
                result = {'success':False , 'code' : '400' , 'msg':f'Something went wrong:{e}'}
            if result['success'] is True:
                print(result['msg'])
            else :
                if result['code'] == 400 :
                    print(result['msg'])
                    print('please try again!')
                    continue
                elif result['code'] == 500:
                    input(result['msg'])
                    exit(1)

if __name__ == "__main__":
    main()
