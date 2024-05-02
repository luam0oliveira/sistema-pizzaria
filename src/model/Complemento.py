from uuid import uuid4


class Complemento:
	def __init__(self, nome:str, valor:float):
		self.__id = uuid4()
		self.__nome = nome
		self.__valor = valor
	

	def getId(self):
		return self.__id
	
	def getNome(self):
		return self.__nome
	
	def setNome(self, nome: str):
		self.__nome = nome
	
	def getValor(self):
		return self.__valor
	
	def setValor(self, valor: float):
		self.__valor = valor