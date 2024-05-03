from model.Banco import Banco
from model.ClienteService import ClienteService
from model.ComplementoService import ComplementoService
from model.Funcionario import Funcionario
from model.FuncionarioService import FuncionarioService
from model.SaborService import SaborService
from view.MenuLogin import MenuLogin
from view.MenuOperacoes import MenuOperacoes


class MenuPrincipalController:
	def __init__(self):
		self.banco = Banco()
		self.clienteService = ClienteService(self.banco)
		self.funcionarioService = FuncionarioService(self.banco)
		self.saborService = SaborService(self.banco)
		self.complementoService = ComplementoService(self.banco) 

	def login(self):
		MenuLogin(self.funcionarioService, self.clienteService)
	
	def operacoes(self):
		MenuOperacoes(
			self.banco.usuario,
			self.clienteService,
			self.funcionarioService,
			self.saborService,
			self.complementoService
		)
