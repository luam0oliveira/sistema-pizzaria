from Pessoa import Pessoa
from uuid import uuid4
from bcrypt import gensalt, hashpw, checkpw


class Usuario(Pessoa):
	def __init__(self, id: int, nome: str, cpf: str, telefone: str, senha: str):
		super(Usuario, self).__init__(nome, cpf, telefone)
		self.__id = id
		self.__login = self.getCpf()
		self.__hashSenha = hashpw(senha.encode(), gensalt(8))
	
	def getId(self):
		return self.__id

	def login(self, senha:str):
		return checkpw(senha.encode(), self.__hashSenha)

	def __str__(self) -> str:
		return f"{self.__login}"