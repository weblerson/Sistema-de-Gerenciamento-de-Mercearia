from config import *

class Category(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key = True, autoincrement = True)
    nome = Column(String(20), nullable = False, default = "sem nome")

class Product(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key = True, autoincrement = True)
    nome = Column(String(20), nullable = False, default = "sem nome")
    idcategoria = Column(Integer, ForeignKey("categoria.id"))
    vendas = Column(Integer)

class Provider(Base):
    __tablename__ = "fornecedor"
    id = Column(Integer, primary_key = True, autoincrement = True)
    nome = Column(String(20), nullable = False, default = "sem nome")
    idcategoria = Column(Integer, ForeignKey("categoria.id"))

class Customer(Base):
    __tablename__ = "cliente"
    nick = Column(String(20), primary_key = True, nullable = False)
    nome = Column(String(60), nullable = False, default = "sem nome")
    cpf = Column(String(11), nullable = False, default = "sem cpf")
    compras = Column(Integer)

class Employee(Base):
    __tablename__ = "funcionario"
    nick = Column(String(20), primary_key = True, nullable = False)
    nome = Column(String(60), nullable = False, default = "sem nome")
    cpf = Column(String(11), nullable = False, default = "sem cpf")

Base.metadata.create_all(engine)