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

# *Rotas de Informação:*

Essas rotas servem para mostrar todas as rotas disponíveis

```Leitura:``` */read* ```Método: GET```   Vai retornar todas as rotas disponíveis para leitura

![image](https://user-images.githubusercontent.com/96087094/158070045-bbafa05b-c030-4353-9718-897460dc51b0.png)

```Filtro:``` */find* ```Método: GET```   Vai retornar todas as rotas e parâmetros disponíveis para filtro

![image](https://user-images.githubusercontent.com/96087094/158070085-30f22807-e213-4ee4-96c4-3f1228af4ba1.png)

```Cadastro:``` */register* ```Método: GET```   Vai retornar todas as rotas e parâmetros disponíveis para cadastro

![image](https://user-images.githubusercontent.com/96087094/158070155-6cc526aa-71ca-4fe8-b32e-a91c278f4aa8.png)

```Alteração:``` */change* ```Método: GET```   Vai retornar todas as rotas e parâmetros disponíveis para alterações

![image](https://user-images.githubusercontent.com/96087094/158070193-12505544-96f8-47da-af37-0a49e33ba002.png)

```Remoção:``` */remove* ```Método: GET```   Vai retornar todas as rotas e parâmetros disponíveis para remoções

![image](https://user-images.githubusercontent.com/96087094/158070236-abfcdd65-17ba-4db9-9a0b-00e5a1deac3c.png)

```Vender:``` */sell* ```Método GET``` Vai retornar a rota e os parâmetros disponíveis para operação de venda

![image](https://user-images.githubusercontent.com/96087094/159334020-389f2823-23d6-42e0-9808-3ecd53292200.png)

```Relatórios:``` */report* ```Método GET``` Vai retornar todas as rotas disponíveis para visualização de relatórios

![image](https://user-images.githubusercontent.com/96087094/159334157-7e726852-ce26-4524-8659-d5d706ca7d8a.png)

# *Rotas de Ação:*
Essas rotas servem para realizar ações, como consultar o banco de dados ou fazer cadastro de produtos, por exemplo.

*Categoria:*

```Leitura:``` */read/category* ```Método: GET```   Vai retornar uma lista com as categorias cadastradas

```Filtro:``` */find/category* ```Método: POST; Parâmetro: id: int```   Vai retornar uma categoria com base no filtro que o usuário passar. A categoria vai ser filtrada pelo respectivo id

```Cadastro:``` */register/category* ```Método: POST, Parâmetro: name: str``` Vai realizar o cadastro de uma nova categoria com o nome passado

```Alteração:``` */change/category* ```Método: POST; Parâmetros: id: int, name: str``` Vai alterar o nome da categoria com o respectivo id passado para o nome digitado

```Remoção:``` */remove/category* ```Método: POST; Parâmetro: id: int``` Vai remover a categoria com o respectivo id passado

*Produto:*

```Leitura:``` */read/product* ```Método: GET``` Vai retornar uma lista com os produtos cadastrados

```Filtro:``` */find/product* ```Método POST; Parâmetro: _id: int``` Vai retornar um produto de acordo com o id que for passado

```Cadastro:``` */register/product* ```Método POST; Parâmetros: name: str, category_id: int``` Vai realizar o cadastro do produto com as informações passadas

```Alteração do Nome:``` */change/productname* ```Método POST; Parâmetros: _id: int, new_name: str``` Vai alterar o nome do produto pelo outro nome passado

```Alteração da Categoria:``` */change/productcategory* ```Método POST; Parâmetros: _id: int, new_category_id: int``` Vai alterar a categoria do produto pela outra categoria passada

```Remoção:``` */remove/product* ```Método POST; Parâmetro: _id: int``` Vai remover o produto de acordo com o id passado

*Fornecedor:*

```Leitura:``` */read/provider* ```Método: GET``` Vai retornar uma lista com os fornecedores cadastrados

```Filtro:``` */find/provider* ```Método POST; Parâmetro: _id: int``` Vai retornar um fornecedor de acordo com o id que for passado

```Cadastro:``` */register/provider* ```Método POST; Parâmetros: name: str, category_id: int``` Vai realizar o cadastro do fornecedor com as informações passadas

```Alteração:``` */change/provider* ```Método POST; Parâmetros: _id: int, name: str``` Vai alterar o nome do fornecedor pelo outro nome passado

```Remoção:``` */remove/provider* ```Método POST; Parâmetro: _id: int``` Vai remover o fornecedor de acordo com o id passado

*Cliente:*

```Leitura:``` */read/customer* ```Método: GET``` Vai retornar uma lista com os clientes cadastrados

```Filtro:``` */find/customer* ```Método POST; Parâmetro: nick: str``` Vai retornar um cliente de acordo com o nick passado

```Cadastro:``` */register/customer* ```Método POST; Parâmetros: nick: str, name: str, cpf: str``` Vai cadastrar um cliente de acordo com as informações passadas

```Alteração:``` */change/customer* ```Método POST; Parâmetros: nick: str, new_nick: str``` Vai alterar o nick de um cliente cadastrado pelo outro nick passado

```Remoção:``` */remove/customer* ```Método POST; Parâmetro: nick: str``` Vai remover o cliente de acordo com o nick passado

*Funcionário:*

```Leitura:``` */read/employee* ```Método: GET``` Vai retornar uma lista com os funcionários cadastrados

```Filtro:``` */find/employee* ```Método POST; Parâmetro: nick: str``` Vai retornar um funcionário de acordo com o nick passado

```Cadastro:``` */find/employee* ```Método POST; Parâmetros: nick: str, name: str, cpf: str``` Vai cadastrar um funcionário de acordo com as informações passadas

```Alteração:``` */change/employee* ```Método POST; Parâmetro: nick: str, new_nick: str``` Vai alterar o nick de um usuário pelo outro nick passado

```Remoção:``` */remove/employee* ```Método POST; Parâmetro: nick: str``` Vai remover o funcionário de acordo com o nick passado

# Operação de Venda de Produto
Esta API pode realizar operações de vendas e deixar registrado no banco de dados com a respectiva data em que foi realizada.

*Rota:*

```Vender:``` */sell* ```Método POST; Parâmetros: product_id: int, customer_nick: str, amount: int``` Vai realizar a operação de venda e registrar com a data do dia em que foi realizada.

# Relatórios
Esta API também pode exibir os relatórios de vendas. Ela era relatórios de vendas por data, relatório de vendas geral de produtos ou de compras de clientes, além de, também, poder fazer um top 3 produtos que mais venderam ou clientes que mais compraram, ordenando do maior para o menor.

*Relatório Geral:*

```Relatório de Vendas de Produtos:``` */report/sales* ```Método GET``` Retorna uma lista com o relatório geral de vendas de produtos.

```Relatório de Compras de Clientes:``` */report/purchases* ```Método GET``` Retorna uma lista com o relatório geral de compras de clientes cadastrados.

*Ranking:*

```Top 3 Produtos:``` */report/sales/ranking* ```Método GET``` Retorna uma lista com o top 3 produtos que mais venderam.

```Top 3 Clientes:``` */report/purchases/ranking* ```Método GET``` Retorna uma lista com o top 3 clientes cadastrados que mais compraram.
