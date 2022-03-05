from config import *
from model import *

class CategoryDAO:
    @classmethod
    def read(cls):
        try:
            category_list = session.query(Category).all()

            return category_list

        except:

            return False

    @classmethod
    def find(cls, id):
        try:
            category = session.query(Category).filter(Category.id == id).one()

            return category

        except:

            return False

    @classmethod
    def register(cls, name):
        try:
            session.add(Category(nome = name))
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change(cls, id, new_name):
        try:
            session.query(Category).filter(Category.id == id).update({Category.nome: new_name})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, id):
        try:
            session.query(Category).filter(Category.id == id).delete()
            session.commit()

            return True

        except:

            return False

class ProductDAO:
    @classmethod
    def read(cls):
        try:
            product_list = session.query(Product).all()

            return product_list

        except:

            return False

    @classmethod
    def find(cls, id):
        try:
            product = session.query(Product).filter(Product.id == id).one()

            return product

        except:

            return False

    @classmethod
    def register(cls, name, category_id):
        try:
            session.add(Product(nome = name, idcategoria = category_id, vendas = 0))
            session.commit()

            return True

        except:
            
            return False

    @classmethod
    def add(cls, id, sales):
        try:
            session.query(Product).filter(Product.id == id).update({Product.vendas: Product.vendas + sales})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change_name(cls, id, new_name):
        try:
            session.query(Product).filter(Product.id == id).update({Product.nome: new_name})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change_category(cls, id, new_category_id):
        try:
            session.query(Product).filter(Product.id == id).update({Product.idcategoria: new_category_id})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, id):
        try:
            session.query(Product).filter(Product.id == id).delete()
            session.commit()

            return True

        except:

            return False

class ProviderDAO:
    @classmethod
    def read(cls):
        try:
            provider_list = session.query(Provider).all()

            return provider_list

        except:

            return False

    @classmethod
    def find(cls, id):
        try:
            provider = session.query(Provider).filter(Provider.id == id).one()

            return provider

        except:

            return False

    @classmethod
    def register(cls, name, category_id):
        try:
            session.add(Provider(nome = name, idcategoria = category_id))
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change(cls, id, new_name):
        try:
            session.query(Provider).filter(Provider.id == id).update({Provider.nome: new_name})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, id):
        try:
            session.query(Provider).filter(Provider.id == id).delete()
            session.commit()

            return True

        except:

            return False

class CustomerDAO:
    @classmethod
    def read(cls):
        try:
            customer_list = session.query(Customer).all()

            return customer_list

        except:

            return False

    @classmethod
    def find(cls, nick):
        try:
            customer = session.query(Customer).filter(Customer.nick == nick).one()

            return customer

        except:

            return False

    @classmethod
    def register(cls, nick, name, cpf):
        try:
            session.add(Customer(nick = nick, nome = name, cpf = cpf, compras = 0))
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change(cls, nick, new_nick):
        try:
            session.query(Customer).filter(Customer.nick == nick).update({Customer.nick: new_nick})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, nick):
        try:
            session.query(Customer).filter(Customer.nick == nick).delete()
            session.commit()

            return True

        except:

            return False

class EmployeeDAO:
    @classmethod
    def read(cls):
        try
            employee_list = session.query(Employee).all()
            
            return employee_list

        except:

            return False

    @classmethod
    def find(cls, nick):
        try:
            employee = session.query(Employee).filter(Employee.nick == nick).one()

            return employee

        except:

            return False

    @classmethod
    def register(cls, nick, name, cpf):
        try:
            session.add(Employee(nick = nick, nome = name, cpf = cpf))
            session.commit()

            return True

        except:
            
            return False

    @classmethod
    def change(cls, nick, new_nick):
        try:
            session.query(Employee).filter(Employee.nick == nick).update({Employee.nick: new_nick})
            session.commit()

            return True

        except:

            return False
        
    @classmethod
    def remove(cls, nick):
        try:
            session.query(Employee).filter(Employee.nick == nick).delete()
            session.commit()

            return True

        except:

            return False