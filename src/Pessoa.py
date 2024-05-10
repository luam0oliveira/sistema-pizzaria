class Pessoa:
	def __init__(self, nome: str, cpf:str, telefone:str):
		self.__nome = nome
		self.__cpf = cpf
		self.__telefone = telefone

	def getNome(self):
		return self.__nome
	
	def setNome(self, nome:str):
		self.__nome = nome

	def getCpf(self):
		return self.__cpf
	
	def setCpf(self, cpf:str):
		self.__cpf = cpf
		
	def getTelefone(self):
		return self.__telefone
	
	def setTelefone(self, telefone:str):
		self.__telefone = telefone
		