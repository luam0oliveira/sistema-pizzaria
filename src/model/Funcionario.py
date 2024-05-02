from model.Usuario import Usuario


class Funcionario(Usuario):
	def __init__(self, nome: str, cpf: str, telefone: str, senha: str, salario: float):
		super().__init__(nome, cpf, telefone, senha)
		self.__salario = salario
	
	def getSalario(self):
		return self.__salario

	def setSalario(self, salario: float):
		self.__salario = salario
