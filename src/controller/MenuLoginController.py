from model.Cliente import Cliente
from model.ClienteService import ClienteService
from model.FuncionarioService import FuncionarioService


class MenuLoginController:
	def __init__(self, funcionarioService:FuncionarioService, clienteService:ClienteService) -> None:
		self.funcionarioService = funcionarioService
		self.clienteService = clienteService
	

	def login_cliente(self, login, senha):
		try:
			self.clienteService.login(login, senha)
			print("Login efetuado com sucesso.")
			return True
		except:
			print("Nao foi possivel fazer login.")

	def login_funcionario(self, login, senha):
		try:
			self.funcionarioService.login(login, senha)
			print("Login efetuado com sucesso.")
			return True
		except:
			print("Nao foi possivel fazer login.")

	def registro_cliente(self, nome, cpf, telefone, senha ):
		try:
			cliente = Cliente(nome, cpf, telefone, senha)
			self.clienteService.criar(cliente)
			return True
		except Exception as e:
			print(e)