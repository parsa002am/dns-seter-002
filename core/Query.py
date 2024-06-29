from core.DataBase import Session
from core.Models import DNS

class DNSQuery:
    
    def __init__(self):
          self.session = Session()
    
    def add_DNS_bulk(self, dnss=[]):
        try:
            
            new_dnss = [DNS(name=dns['name'] , primary_dns=dns['primary_dns'] , secondary_dns = dns['primary_dns']) for dns in dnss]
            self.session.bulk_save_objects(new_dnss)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
    def get_id(self , input_id):
        try:
            return self.session.query(DNS).get(id=input_id)
        finally:
            self.session.close()
    
    def get_all_dns(self):
        try:
            return self.session.query(DNS).all()
        except:
            return []
        finally:
            self.session.close()
    
    def add_dns(self,name,primary_dns , secondary_dns):
        try:
            new_dns = DNS(name=name , primary_dns=primary_dns , secondary_dns = secondary_dns)
            self.session.add(new_dns)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
    def delete_dns(self,id):
        try:
            admin= self.session.query(DNS).filter_by(id=id).first()
            if admin :
                self.session.delete(admin)
                self.session.commit()
                return True
            else:
                return False
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()