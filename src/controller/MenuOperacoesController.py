from model.Cliente import Cliente
from model.ClienteService import ClienteService
from model.ComplementoService import ComplementoService
from model.Funcionario import Funcionario
from model.FuncionarioService import FuncionarioService
from model.SaborService import SaborService
from utils import emptyToNone


class MenuOperacoesController:
	def __init__(self,
			  clienteService: ClienteService,
			  funcionarioService:FuncionarioService = None,
			  saborService: SaborService = None,
			  complementoService: ComplementoService = None):
		self.funcionarioService = funcionarioService
		self.clienteService = clienteService
	

	def adicionar_funcionario(self, nome, cpf, telefone, senha, salario):
		try:

			funcionario = Funcionario(nome, cpf, telefone, senha, salario)
			self.funcionarioService.criar(funcionario)
			print("Funcionário cadastrado com sucesso.")
			return True
		except:
			print("Nao foi possivel fazer login.")

	def editar_funcionario(self, nome, cpf, telefone, salario):
		try:
			funcionario = Funcionario(emptyToNone(nome), cpf, emptyToNone(telefone), "", emptyToNone(salario))
			
			self.funcionarioService.editar(funcionario)
			print(self.funcionarioService.procurarPorCpf(cpf))
			return True
		except Exception as e:
			print(e)
			



	# def login_funcionario(self, login, senha):
	# 	try:
	# 		self.funcionarioService.login(login, senha)
	# 		print("Login efetuado com sucesso.")
	# 		return True
	# 	except:
	# 		print("Nao foi possivel fazer login.")

	# def registro_cliente(self, nome, cpf, telefone, senha ):
	# 	try:
	# 		cliente = Cliente(nome, cpf, telefone, senha)
	# 		self.clienteService.criar(cliente)
	# 		return True
	# 	except Exception as e:
	# 		print(e)