from Usuario import Usuario


class Funcionario(Usuario):
	def __init__(self, id:int, nome: str, cpf: str, telefone: str, senha: str, salario: float):
		super().__init__(id, nome, cpf, telefone, senha)
		self.__salario = salario
	
	def getSalario(self):
		return self.__salario

	def setSalario(self, salario: float):
		self.__salario = salario

	def __str__(self) -> str:
		return f"Nome: {self.getNome()}, CPF:{self.getCpf()}, telefone: {self.getTelefone()}"
