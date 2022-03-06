from fastapi import FastAPI
from controller import *

app = FastAPI()

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