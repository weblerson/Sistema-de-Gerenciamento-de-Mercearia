from fastapi import FastAPI
from controller import *

app = FastAPI()

#---------------Category---------------

@app.get('/read/category')
def read_category():
    response = CategoryController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if len(response) == 0:
        return {"response": "Não há nenhuma categoria cadastrada."}

    return response

@app.post('/find/category')
def find_category(_id: int):
    response = CategoryController.find(_id = _id)

    if not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    return {"id": response.id, "nome": response.nome}

@app.post('/register/category')
def register_category(name: str):
    response = CategoryController.register(name = name)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Categoria cadastrada com sucesso."}

@app.post('/change/category')
def change_category(_id, name):
    response = CategoryController.change(_id = _id, new_name = name)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Categoria alterada com sucesso."}

@app.post('/remove/category')
def remove_category(_id):
    response = CategoryController.remove(_id = _id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados"}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Categoria removida com sucesso."}

#---------------Category---------------

#---------------Product---------------

@app.get('/read/product')
def read_product():
    response = ProductController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if len(response) == 0:
        return {"response": "Não há nenhum produto cadastrado."}

    return {"response": response}

@app.post('/find/product')
def find_product(_id: int):
    response = ProductController.find(_id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    return {"nome": response.nome, "idcategoria": response.idcategoria, "id": response.id, "vendas": response.vendas}

@app.post('/register/product')
def register_product(name: str, category_id: int):
    response = ProductController.register(name = name, category_id = category_id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Produto cadastrado com sucesso"}

@app.post('/change/productname')
def change_product_name(_id: int, new_name: str):
    response = ProductController.change_name(_id = _id, new_name = new_name)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Nome do produto alterado com sucesso."}

@app.post('/change/productcategory')
def change_product_category(_id: int, new_category_id: int):
    response = ProductController.change_category(_id = _id, new_category_id = category_id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Categoria do produto alterada com sucesso."}

@app.post('/remove/product')
def remove_product(_id: int):
    response = ProductController.remove(_id = _id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Produto removido com sucesso."}

#---------------Product---------------

#---------------Provider---------------

@app.get('/read/provider')
def read_provider():
    response = ProviderController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if len(response) == 0:
        return {"response": "Não há nenhum fornecedor cadastrado."}

    return response

@app.post('/find/provider')
def find_provider(_id: int):
    response = ProviderController.find(_id = _id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    return {"response": {"nome": response.nome, "idcategoria": response.idcategoria, "id": response.id}}

@app.post('/register/provider')
def register_provider(name: str, category_id: int):
    response = ProviderController.register(name = name, category_id = category_id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Fornecedor cadastrado com sucesso."}

@app.post('/change/provider')
def change_provider(_id: int, name: str):
    response = ProviderController.change(_id = _id, new_name = name)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Fornecedor alterado com sucesso."}

@app.post('/remove/provider')
def remove_provider(_id: int):
    response = ProviderController.remove(_id = _id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Fornecedor removido com sucesso."}

#---------------Provider---------------

#---------------Customer---------------

@app.get('/read/customer')
def read_customer():
    response = CustomerController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    return {"response": response}

@app.post('/find/customer')
def find_customer(nick: str):
    response = CustomerController.find(nick = nick)
    
    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    return {"response": {"nick": response.nick, "nome": response.nome, "CPF": response.cpf, "compras": response.compras}}

@app.post('/register/customer')
def register_customer(nick: str, name: str, cpf: str):
    response = CustomerController.register(nick = nick, name = name, cpf = cpf)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Cliente cadastrado com sucesso."}

@app.post('/change/customer')
def change_customer(nick: str, new_nick: str):
    response = CustomerController.change(nick = nick, new_nick = new_nick)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Nick do cliente alterado com sucesso."}

@app.post('remove/customer')
def remove_customer(nick: str):
    response = CustomerController.remove(nick = nick)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Cliente removido com sucesso."}

#---------------Customer---------------

#---------------Employee---------------

@app.get('/read/employee')
def read_employee():
    response = EmployeeController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    return {"response": response}

@app.post('/find/employee')
def find_employee(nick: str):
    response = EmployeeController.find(nick = nick)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    return {"response": {"nick": response.nick, "nome": response.nome, "CPF": response.cpf}}

@app.post('/register/employee')
def register_employee(nick: str, name: str, cpf: str):
    response = EmployeeController.register(nick = nick, name = name, cpf = cpf)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Funcionário cadastrado com sucesso"}

@app.post('/change/employee')
def change_employee(nick: str, new_nick: str):
    response = EmployeeController.change(nick = nick, new_nick = new_nick)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}
    
    if type(response) == bool and response:
        return {"response": "Nick de funcionário alterado com sucesso."}

@app.post('/remove/employees/')
def remove_employee(nick: str):
    response = EmployeeController.remove(nick = nick)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Funcionário removido com sucesso."}

#---------------Employee---------------

#---------------Sales---------------

@app.get('/sales')
def read_sales():
    response = SalesController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o bando de dados."}

    if len(response) == 0:
        return {"response": "Não há nenhuma venda registrada."}

    return {"response": response}

#---------------Sales---------------

#---------------Info---------------

@app.get('/read')
def read():
    return {"response": {"rotas": "/category, /product, /provider, /customer, /employee"}}

@app.get('/find')
def find():
    return {"response": {"rotas": "/category (_id: int), /product (_id: int), /provider (_id: int), /customer (nick: str), /employee (nick: str)"}}

@app.get('/register')
def register():
    return {"response": {"rotas": "/category (name: str), /product (name: str, category_id: int), /provider (name: str, category_id: int), /customer (nick: str, name: str, cpf: str), /employee (nick: str, name: str, cpf: str)"}}

@app.get('/change')
def change():
    return {"response": {"rotas": "/category (_id: int, new_name: str), /productname (_id: int, new_name: str), /productcategory (_id: int, new_category_id: int), /provider (_id: int, name: str), /customer (nick: str, new_nick: str), /employee (nick: str, new_nick: str)"}}

@app.get('/remove')
def remove():
    return {"response": {"rotas": "/category (_id: int), /product (_id: int), /provider (_id: int), /customer (nick: str), /employee (nick: str)"}}

@app.get('/sell')
def info_sell():
    return {"response": {"rotas": "/sell (product_id: int, customer_nick: str, amount: int)"}}

@app.get('/report')
def report():
    return {"response": {"rotas": "/report/sales, /report/sales/ranking, /report/purchases, /report/purchases/ranking"}}

#---------------Info---------------

#---------------Special---------------

@app.post('/sell')
def sell(product_id: int, customer_nick: str, amount: int):
    customer_response = CustomerController.buy(nick = customer_nick, amount = amount)
    product_response = ProductController.sell(_id = product_id, amount = amount)
    sales_response = SalesController.add(amount = amount)

    if type(customer_response) == bool and not customer_response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados do cliente."}

    elif type(product_response) == bool and not product_response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados do produto."}

    elif type(sales_response) == bool and not sales_response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados de vendas."}


    if type(customer_response) == str:
        return {"response": customer_response}

    elif type(product_response) == str:
        return {"response": product_response}
    

    if (type(customer_response) == bool and customer_response) and (type(product_response) == bool and product_response) and (type(sales_response) == bool and sales_response):
        return {"response": "Venda realizada com sucesso."}

#---------------Special---------------

#---------------Report---------------

@app.get('/report/sales')
def sales():
    response = ProductController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    sales = []

    for product in response:
        sales.append({"nome": product.nome, "vendas": product.vendas})

    return {"response": sales}

@app.get('/report/sales/ranking')
def product_sales():
    response = ProductController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    response.sort(reverse = True, key = lambda x: x.vendas)

    sales = []

    for product in response:
        sales.append({"nome": product.nome, "vendas": product.vendas})

        if len(sales) == 3:
            break

    return {"response": {
        "#1": sales[0],
        "#2": sales[1],
        "#3": sales[2]
    }}

@app.get('/report/purchases')
def purchases():
    response = CustomerController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    purchases = []

    for customer in response:
        purchases.append({"nick": customer.nick, "compras": customer.compras})

    return {"response": purchases}

@app.get('/report/purchases/ranking')
def customer_purchases():
    response = CustomerController.read()

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    response.sort(reverse = True, key = lambda x: x.compras)

    purchases = []

    for customer in response:
        purchases.append({"nick": customer.nick, "compras": customer.compras})

        if len(purchases) == 3:
            break

    return {"response": {
        "#1": purchases[0],
        "#2": purchases[1],
        "#3": purchases[2]
    }}

#---------------Report---------------
