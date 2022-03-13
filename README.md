# Sistema de Gerenciamento de Mercearia
Sistema de gerenciamento de mercearia que usa o banco de dados SQLite e exibe os dados por meio de API, para a interface ser construída a partir de qualquer linguagem.

# Instalação das Bibliotecas
Para utilizar a API, instale todas as bibliotecas necessárias passando o comando ```pip install -r requirements.txt``` no terminal na raiz do projeto.

# Criação do Servidor
Para criar o servidor, após a instalação das biblitecas, digite o comando ```uvicorn API:app``` no terminal também na raiz do projeto.

Uma interface como essa irá aparecer no terminal, indicando que tudo deu certo:

![image](https://user-images.githubusercontent.com/96087094/158069341-3303a0ad-12e7-46a9-8960-dcce9ada8ed1.png)

Agora, o servidor vai estar aberto. Para consumir a API, basta fazer requisições para o host ```http://127.0.0.1:8000``` com as rotas.

# Rotas
Esta API possui diversas rotas feitas para as mais diversas coisas, como fazer a leitura do banco de dados sobre os produtos cadastrados, clientes, ou até mesmo para fazer o cadastro de um funcionário.

Aqui vai a listagem das rotas disponíveis:

*Informação:*

Essas rotas servem para mostrar todas as rotas disponíveis

```Leitura:``` /read ```Método: GET```   Vai retornar todas as rotas disponíveis para leitura

![image](https://user-images.githubusercontent.com/96087094/158070045-bbafa05b-c030-4353-9718-897460dc51b0.png)

```Filtro:``` /find ```Método: GET```   Vai retornar todas as rotas e parâmetros disponíveis para filtro

![image](https://user-images.githubusercontent.com/96087094/158070085-30f22807-e213-4ee4-96c4-3f1228af4ba1.png)

```Cadastro:``` /register ```Método: GET```   Vai retornar todas as rotas e parâmetros disponíveis para cadastro

![image](https://user-images.githubusercontent.com/96087094/158070155-6cc526aa-71ca-4fe8-b32e-a91c278f4aa8.png)

```Alteração:``` /change ```Método GET```   Vai retornar todas as rotas e parâmetros disponíveis para alterações

![image](https://user-images.githubusercontent.com/96087094/158070193-12505544-96f8-47da-af37-0a49e33ba002.png)

```Remoção:``` /remove ```Método GET```   Vai retornar todas as rotas e parâmetros disponíveis para remoções

![image](https://user-images.githubusercontent.com/96087094/158070236-abfcdd65-17ba-4db9-9a0b-00e5a1deac3c.png)

*Categoria:*

```Leitura:``` /read/category ```Método: GET```   Vai retornar uma lista com as categorias cadastradas

```Filtro:``` /find/category ```Método> POST; Parâmetro: ```   Vai retornar uma categoria com base no filtro que o usuário passar. A categoria vai ser filtrada pelo respectivo ID