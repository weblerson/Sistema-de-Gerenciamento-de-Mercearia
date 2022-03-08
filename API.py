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
def find_category(id: int):
    response = CategoryController.find(id = id)

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
def change_category(id, name):
    response = CategoryController.change(id = id, new_name = name)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Categoria alterada com sucesso."}

@app.post('/remove/category')
def remove_category(id):
    response = CategoryController.remove(id = id)

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

    return response

@app.post('/find/product')
def find_product(id: int):
    response = ProductController.find(id)

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
def change_product_name(id: int, name: str):
    response = ProductController.change_name(id = id, new_name = name)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Nome do produto alterado com sucesso."}

@app.post('/change/productcategory')
def change_product_category(id: int, category_id: int):
    response = ProductController.change_category(id = id, new_category_id = category_id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Categoria do produto alterada com sucesso."}

@app.post('/remove/product')
def remove_product(id: int):
    response = ProductController.remove(id = id)

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
def find_provider(id: int):
    response = ProviderController.find(id = id)

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
def change_provider(id: int, name: str):
    response = ProviderController.change(id = id, new_name = name)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Fornecedor alterado com sucesso."}

@app.post('/remove/provider')
def remove_provider(id: int):
    response = ProviderController.remove(id = id)

    if type(response) == bool and not response:
        return {"response": "Ocorreu um erro ao consultar o banco de dados."}

    if type(response) == str:
        return {"response": response}

    if type(response) == bool and response:
        return {"response": "Fornecedor removido com sucesso."}

#---------------Provider---------------

#---------------Special---------------



#---------------Special---------------