from core.DataBase import Session
from core.Models import DNS

class DNSQuery:
    
    def __init__(self):
          self.session = Session()
    
    def add_DNS_bulk(self, dnss=[]):
        try:
            
            new_dnss = [DNSQuery(name=dns['name'] , dns_primary=dns['dns_primary'] , dns_secondary = dns['dns_secondary']) for dns in dnss]
            self.session.bulk_save_objects(new_dnss)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
    def get_id(self , input_id):
        try:
            return self.session.query(DNSQuery).filter_by(id=input_id).first().value
        finally:
            self.session.close()