from config import *
from model import *

class CategoryController:
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
            if not session.query(session.query(Category).filter(Category.id == id).exists()).one()[0]:
                return f"Não existe nenhuma categoria com id {id}."

        except:
            return False

        try:
            category = session.query(Category).filter(Category.id == id).one()

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
    def change(cls, id, new_name):
        try:
            if not session.query(session.query(Category).filter(Category.id == id).exists()).one()[0]:
                return f"A categoria com id {id} não existe. Impossível fazer a alteração."

        except:
            return False

        try:
            if session.query(session.query(Category).filter(Category.nome == new_name).exists()).one()[0]:
                return f"Já existe uma categoria de nome {new_name} cadastrada. Não é possível fazer a alteração:"

        except:
            return False

        try:
            session.query(Category).filter(Category.id == id).update({Category.nome: new_name})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, id):
        try:
            if not session.query(session.query(Category).filter(Category.id == id).exists()).one()[0]:
                return f"Não existe nenhuma categoria de id {id} cadastrada. Impossível fazer a remoção."

        except:
            return False

        try:
            session.query(Category).filter(Category.id == id).delete()
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
    def find(cls, id):
        try:
            if not session.query(session.query(Product).filter(Product.id == id).exists()).one()[0]:
                return f"Não existe nenhum produto de id {id} cadastrado."

        except:
            return False

        try:
            product = session.query(Product).filter(Product.id == id).one()

            return product

        except:

            return False

    @classmethod
    def register(cls, name, category_id):
        try:
            if session.query(session.query(Product).filter(Product.nome == name).exists()).one()[0]:
                return f"Um produto de nome {name} já existe. Não é possível realizar o cadastro."

            if not session.query(session.query(Category).filter(Category.id == category_id).exists()).one()[0]:
                return f"Não existe nenhuma categoria de id {id}. Impossível realizar o cadastro."

        except:
            return False

        try:
            session.add(Product(nome = name, idcategoria = category_id, vendas = 0))
            session.commit()

            return True

        except:
            
            return False

    @classmethod
    def add(cls, id, sales):
        try:
            if not session.query(session.query(Product).filter(Product.id == id).exists()).one()[0]:
                return f"Não existe nenhum produto de id {id} cadastrado. Impossível fazer a adição."

        except:
            return False

        try:
            session.query(Product).filter(Product.id == id).update({Product.vendas: Product.vendas + sales})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change_name(cls, id, new_name):
        try:
            if not session.query(session.query(Product).filter(Product.id == id).exists()).one()[0]:
                return f"O produto de id {id} não existe. Impossível fazer a alteração."

            if session.query(session.query(Product).filter(Product.nome == name).exists()).one()[0]:
                return f"Um produto de nome {new_name} já existe. Impossível fazer a alteração."

        except:
            return False

        try:
            session.query(Product).filter(Product.id == id).update({Product.nome: new_name})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change_category(cls, id, new_category_id):
        try:
            if not session.query(session.query(Product).filter(Product.id == id).exists()).one()[0]:
                return f"Não existe nenhum produto de id {id} cadastrado. Impossível fazer a alteração."

            if not session.query(session.query(Category).filter(Category.id == new_category_id).exists()).one()[0]:
                return f"Não existe nenhuma categoria cadastrada de id {id}. Impossível fazer a alteração."

        except:
            return False

        try:
            session.query(Product).filter(Product.id == id).update({Product.idcategoria: new_category_id})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, id):
        try:
            if not session.query(session.query(Product).filter(Product.id == id).exists()).one()[0]:
                return f"Não existe nenhum produto de id {id} cadastrado. Impossível fazer a remoção."

        except:
            return False

        try:
            session.query(Product).filter(Product.id == id).delete()
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
    def find(cls, id):
        try:
            if not session.query(session.query(Provider).filter(Provider.id == id).exists()).one()[0]:
                return f"Não existe nenhum fornecedor de id {id} cadastrado."

        except:
            return False

        try:
            provider = session.query(Provider).filter(Provider.id == id).one()

            return provider

        except:

            return False

    @classmethod
    def register(cls, name, category_id):
        try:
            if session.query(session.query(Provider).filter(Provider.nome == name).exists()).one()[0]:
                return f"Já existe um fornecedor de nome {name} cadastrado. Impossível realizar o cadastro."

            if not session.query(session.query(Category).filter(Category.id == category_id).exists()).one()[0]:
                return f"Não existe nenhuma categoria de id {id} cadastrada. Impossível realizar o cadastro."

        except:
            return False

        try:
            session.add(Provider(nome = name, idcategoria = category_id))
            session.commit()

            return True

        except:

            return False

    @classmethod
    def change(cls, id, new_name):
        try:
            if not session.query(session.query(Provider).filter(Provider.id == id).exists()).one()[0]:
                return f"Não existe nenhum fornecedor de id {id} cadastrado. Impossível realizar a alteração."

        except:
            return False

        try:
            session.query(Provider).filter(Provider.id == id).update({Provider.nome: new_name})
            session.commit()

            return True

        except:

            return False

    @classmethod
    def remove(cls, id):
        try:
            if not session.query(session.query(Provider).filter(Provider.id == id).exists()).one()[0]:
                return f"Não existe nenhum fornecedor de id {id} cadastrado. Impossível fazer a remoção."

        except:
            return False

        try:
            session.query(Provider).filter(Provider.id == id).delete()
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

        try:
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

        try:
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