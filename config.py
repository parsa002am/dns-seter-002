import os
from core.Query import DNSQuery

DATA_FOLDER = 'DNS002'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

file_name = f'{DATA_FOLDER}/002DNS.txt'

DEFAULT_DNS = [
    {
        'name': '403.ONLINE ',
        'primary_dns': '10.202.10.202',
        'secondary_dns' : '10.202.10.102'
    },
    {
        'name': 'shecan',
        'primary_dns': '10.202.10.202',
        'secondary_dns' : '10.202.10.102'
    },
    {
        'name': 'beshkan',
        'primary_dns': '181.41.194.177',
        'secondary_dns' : '181.41.194.186'
    },
    {
        'name': 'begzar',
        'primary_dns': '185.55.226.26',
        'secondary_dns' : '185.55.225.25'
    },
    {
        'name': 'Google Public DNS servers',
        'primary_dns': '8.8.8.8',
        'secondary_dns' : '8.8.4.4'
    }

    
]

if not os.path.isfile(file_name):
    try:
        print('welcome to 002 DNS\n\n Coded by parsa002am@gmail.com')
        DNSQuery().add_DNS_bulk(DEFAULT_DNS)
        with open(file_name,'w') as file:
                file.write('Coded by Parsa002 \n email: parsa002am@gmail.com \n telegram: http://t.me/parsa002am \n dont try for remove it !')
        
    except:
        print('have some error')
        exit()