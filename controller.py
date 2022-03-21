from config import *
from model import *
import datetime

class CategoryController:
    @classmethod
    def read(cls):
        try:
            category_list = session.query(Category).all()

            return category_list

        except:

            return False

    @classmethod
    def find(cls, _id):
        try:
            if not session.query(session.query(Category).filter(Category.id == _id).exists()).one()[0]:
                return f"Não existe nenhuma categoria com id {_id}."

        except:
            return False

        try:
            category = session.query(Category).filter(Category.id == _id).one()

            return category

        except:

            return False

    @classmethod
    def register(cls, name):
        try:
            if session.query(session.query(Category).filter(Category.nome == name).exists()).one()[0]:
                return f"A categoria {name} já existe. Não é possível fazer o cadastro."

        except:
            return False

        try:
            session.add(Category(nome = name))
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change(cls, _id, new_name):
        try:
            if not session.query(session.query(Category).filter(Category.id == _id).exists()).one()[0]:
                return f"A categoria com id {_id} não existe. Impossível fazer a alteração."

        except:
            return False

        try:
            if session.query(session.query(Category).filter(Category.nome == new_name).exists()).one()[0]:
                return f"Já existe uma categoria de nome {new_name} cadastrada. Não é possível fazer a alteração:"

        except:
            return False

        try:
            session.query(Category).filter(Category.id == _id).update({Category.nome: new_name})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, _id):
        try:
            if not session.query(session.query(Category).filter(Category.id == _id).exists()).one()[0]:
                return f"Não existe nenhuma categoria de id {_id} cadastrada. Impossível fazer a remoção."

        except:
            return False

        try:
            session.query(Category).filter(Category.id == _id).delete()
            session.commit()

            return True

        except:

            return False

class ProductController:
    @classmethod
    def read(cls):
        try:
            product_list = session.query(Product).all()

            return product_list

        except:

            return False

    @classmethod
    def find(cls, _id):
        try:
            if not session.query(session.query(Product).filter(Product.id == _id).exists()).one()[0]:
                return f"Não existe nenhum produto de id {_id} cadastrado."

        except:
            return False

        try:
            product = session.query(Product).filter(Product.id == _id).one()

            return product

        except:

            return False

    @classmethod
    def register(cls, name, category_id):
        try:
            if session.query(session.query(Product).filter(Product.nome == name).exists()).one()[0]:
                return f"Um produto de nome {name} já existe. Não é possível realizar o cadastro."

            if not session.query(session.query(Category).filter(Category.id == category_id).exists()).one()[0]:
                return f"Não existe nenhuma categoria de id {_id}. Impossível realizar o cadastro."

        except:
            return False

        try:
            session.add(Product(nome = name, idcategoria = category_id, vendas = 0))
            session.commit()

            return True

        except:
            
            return False

    @classmethod
    def sell(cls, _id, amount):
        try:
            if not session.query(session.query(Product).filter(Product.id == _id).exists()).one()[0]:
                return f"Não existe nenhum produto de id {_id} cadastrado. Impossível fazer a adição."

        except:
            return False

        try:
            session.query(Product).filter(Product.id == _id).update({Product.vendas: Product.vendas + amount})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change_name(cls, _id, new_name):
        try:
            if not session.query(session.query(Product).filter(Product.id == _id).exists()).one()[0]:
                return f"O produto de id {_id} não existe. Impossível fazer a alteração."

            if session.query(session.query(Product).filter(Product.nome == new_name).exists()).one()[0]:
                return f"Um produto de nome {new_name} já existe. Impossível fazer a alteração."

        except:
            return False

        try:
            session.query(Product).filter(Product.id == _id).update({Product.nome: new_name})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change_category(cls, _id, new_category_id):
        try:
            if not session.query(session.query(Product).filter(Product.id == _id).exists()).one()[0]:
                return f"Não existe nenhum produto de id {_id} cadastrado. Impossível fazer a alteração."

            if not session.query(session.query(Category).filter(Category.id == new_category_id).exists()).one()[0]:
                return f"Não existe nenhuma categoria cadastrada de id {_id}. Impossível fazer a alteração."

        except:
            return False

        try:
            session.query(Product).filter(Product.id == _id).update({Product.idcategoria: new_category_id})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, _id):
        try:
            if not session.query(session.query(Product).filter(Product.id == _id).exists()).one()[0]:
                return f"Não existe nenhum produto de id {_id} cadastrado. Impossível fazer a remoção."

        except:
            return False

        try:
            session.query(Product).filter(Product.id == _id).delete()
            session.commit()

            return True

        except:

            return False

class ProviderController:
    @classmethod
    def read(cls):
        try:
            provider_list = session.query(Provider).all()

            return provider_list

        except:

            return False

    @classmethod
    def find(cls, _id):
        try:
            if not session.query(session.query(Provider).filter(Provider.id == _id).exists()).one()[0]:
                return f"Não existe nenhum fornecedor de id {_id} cadastrado."

        except:
            return False

        try:
            provider = session.query(Provider).filter(Provider.id == _id).one()

            return provider

        except:

            return False

    @classmethod
    def register(cls, name, category_id):
        try:
            if session.query(session.query(Provider).filter(Provider.nome == name).exists()).one()[0]:
                return f"Já existe um fornecedor de nome {name} cadastrado. Impossível realizar o cadastro."

            if not session.query(session.query(Category).filter(Category.id == category_id).exists()).one()[0]:
                return f"Não existe nenhuma categoria de id {_id} cadastrada. Impossível realizar o cadastro."

        except:
            return False

        try:
            session.add(Provider(nome = name, idcategoria = category_id))
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change(cls, _id, new_name):
        try:
            if not session.query(session.query(Provider).filter(Provider.id == _id).exists()).one()[0]:
                return f"Não existe nenhum fornecedor de id {_id} cadastrado. Impossível realizar a alteração."

        except:
            return False

        try:
            session.query(Provider).filter(Provider.id == _id).update({Provider.nome: new_name})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, _id):
        try:
            if not session.query(session.query(Provider).filter(Provider.id == _id).exists()).one()[0]:
                return f"Não existe nenhum fornecedor de id {_id} cadastrado. Impossível fazer a remoção."

        except:
            return False

        try:
            session.query(Provider).filter(Provider.id == _id).delete()
            session.commit()

            return True

        except:

            return False

class CustomerController:
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
            if not session.query(session.query(Customer).filter(Customer.nick == nick).exists()).one()[0]:
                return f"Não existe nenhum cliente de nick {nick} cadastrado."

        except:
            return False

        try:
            customer = session.query(Customer).filter(Customer.nick == nick).one()

            return customer

        except:

            return False

    @classmethod
    def register(cls, nick, name, cpf):
        try:
            if session.query(session.query(Customer).filter(Customer.nick == nick).exists()).one()[0]:
                return f"Um cliente de nick {nick} já existe. Impossível realizar o cadastro."

            if session.query(session.query(Customer).filter(Customer.cpf == cpf).exists()).one()[0]:
                return "Já existe um cliente cadastrado com o CPF passado. Impossível realizar o cadastro."

        except:
            return False

        cpf = cpf.replace('-', '')

        try:
            if len(cpf) < 11 or len(cpf) > 11:
                return "CPF passado inválido. Digite um CPF de 11 dígitos."

            session.add(Customer(nick = nick, nome = name, cpf = cpf, compras = 0))
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change(cls, nick, new_nick):
        try:
            if not session.query(session.query(Customer).filter(Customer.nick == nick).exists()).one()[0]:
                return f"O cliente com nick {nick} não existe. Impossível fazer a alteração."

            if session.query(session.query(Customer).filter(Customer.nick == new_nick).exists()).one()[0]:
                return f"Já existe um cliente com nick {nick} cadastrado. Impossível alterar."

        except:
            return False

        try:
            session.query(Customer).filter(Customer.nick == nick).update({Customer.nick: new_nick})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, nick):
        try:
            if not session.query(session.query(Customer).filter(Customer.nick == nick).exists()).one()[0]:
                return f"O cliente de nick {nick} não existe. Não é possível fazer a remoção."

        except:
            return False

        try:
            session.query(Customer).filter(Customer.nick == nick).delete()
            session.commit()

            return True

        except:

            return False

    @classmethod
    def buy(cls, nick, amount):
        try:
            if not session.query(session.query(Customer).filter(Customer.nick == nick).exists()).one()[0]:
                return f"O cliente de nick {nick} não existe. Não é possível fazer a operação de venda."
            
        except:
            return False

        try:
            session.query(Customer).filter(Customer.nick == nick).update({Customer.compras: Customer.compras + amount})
            session.commit()

            return True

        except:

            return False

class EmployeeController:
    @classmethod
    def read(cls):
        try:
            employee_list = session.query(Employee).all()
            
            return employee_list

        except:

            return False

    @classmethod
    def find(cls, nick):
        try:
            if not session.query(session.query(Employee).filter(Employee.nick == nick).exists()).one()[0]:
                return f"Não existe nenhum funcionário de nick {nick} cadastrado."

        except:
            return False

        try:
            employee = session.query(Employee).filter(Employee.nick == nick).one()

            return employee

        except:

            return False

    @classmethod
    def register(cls, nick, name, cpf):
        try:
            if session.query(session.query(Employee).filter(Employee.nick == nick).exists()).one()[0]:
                return f"Já existe um funcionário com nick {nick} cadastrado. Não é possível realizar o cadastro."

            if session.query(session.query(Employee).filter(Employee.cpf == cpf).exists()).one()[0]:
                return "O CPF digitado já foi cadastrado. Não é possível realizar o cadastro."

        except:
            return False

        cpf = cpf.replace('-', '')

        try:
            if len(cpf) < 11 or len(cpf) > 11:
                return "CPF passado inválido. Digite um CPF de 11 dígitos."

            session.add(Employee(nick = nick, nome = name, cpf = cpf))
            session.commit()

            return True

        except:
            
            return False

    @classmethod
    def change(cls, nick, new_nick):
        try:
            if not session.query(session.query(Employee).filter(Employee.nick == nick).exists()).one()[0]:
                return f"Não existe nenhum funcionário de nick {nick} cadastrado. Impossível fazer a alteração."

            if session.query(session.query(Employee).filter(Employee.nick == new_nick).exists()).one()[0]:
                return f"Já existe um funcionário com o nick {nick} cadastrado. Impossível realizar a alteração."

        except:
            return False

        try:
            session.query(Employee).filter(Employee.nick == nick).update({Employee.nick: new_nick})
            session.commit()

            return True

        except:

            return False
        
    @classmethod
    def remove(cls, nick):
        try:
            if not session.query(session.query(Employee).filter(Employee.nick == nick).exists()).one()[0]:
                return f"Não existe nenhum funcionário de nick {nick}. Impossível fazer a remoção."

        except:
            return False

        try:
            session.query(Employee).filter(Employee.nick == nick).delete()
            session.commit()

            return True

        except:

            return False

class SalesController:
    @classmethod
    def read(cls):
        try:
            sales_list = session.query(Sales).all()

            return sales_list

        except:
            return False

    @classmethod
    def add(cls, amount):
        today = lambda: str(datetime.date.today()).replace('-', '/')

        if not session.query(session.query(Sales).filter(Sales.data == today()).exists()).one()[0]:
            try:
                session.add(Sales(data = today(), vendas = amount))
                session.commit()

                return True

            except:
                return False

        else:
            try:
                session.query(Sales).filter(Sales.data == today()).update({Sales.vendas: Sales.vendas + amount})
                session.commit()

                return True

            except:
                return False
