from model.Banco import Banco
from model.ClienteService import ClienteService
from model.FuncionarioService import FuncionarioService
from view.MenuLogin import MenuLogin


class MenuPrincipalController:
	def __init__(self):
		self.banco = Banco()
		self.clienteService = ClienteService(self.banco)
		self.funcionarioService = FuncionarioService(self.banco)

	def login(self):
		MenuLogin(self.funcionarioService, self.clienteService)
