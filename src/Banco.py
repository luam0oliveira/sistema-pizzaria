from model.Cliente import Cliente
from model.Complemento import Complemento
from model.Funcionario import Funcionario
from model.Sabor import Sabor


class Banco:
	def __init__(self):
		self.clientes = {'1': Cliente("dmt", '1', "123", '1')}
		self.funcionarios = {'0': Funcionario("adm", '0', '0', '0', 100)}
		self.sabores = {'1': Sabor("Cala,bresa", 5, '1'), '2': Sabor("Calafrango", 7, '2'), '3': Sabor("TacumFome", 10, '3')}
		self.complementos = {'1': Complemento("TacumSede", 10, '1'), '2':Complemento("Água", 8, '2')}
		self.usuario = None
