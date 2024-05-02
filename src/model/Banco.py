from model.Funcionario import Funcionario


class Banco:
	def __init__(self):
		self.clientes = {}
		self.funcionarios = {'0': Funcionario("adm", '0', '0', '0', 100)}
		self.sabores = {}
		self.complementos = {}
		self.usuario = None
