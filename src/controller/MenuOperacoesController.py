from model.Cliente import Cliente
from model.ClienteService import ClienteService
from model.ComplementoService import ComplementoService
from model.Funcionario import Funcionario
from model.FuncionarioService import FuncionarioService
from model.Sabor import Sabor
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
		self.saborService = saborService
	

	def listar_funcionarios(self):
		try:
			funcionarios = self.funcionarioService.listar()
			return funcionarios
		except:
			print("!!!")

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
			# print(self.funcionarioService.procurarPorCpf(cpf))
			return True
		except Exception as e:
			print(e)
			
	def excluir_funcionario(self, cpf):
		try:
			funcionario = self.funcionarioService.procurarPorCpf(cpf)

			if not funcionario:
				raise Exception("Funcionário não existe.")
			
			self.funcionarioService.excluir(funcionario)
			return True
		except Exception as e:
			print(e)
			

	def adicionar_sabor(self, nome, valor):
		try:
			sabor = Sabor(nome, valor)
			if self.saborService.criar(sabor):
				print("Criado com sucesso")
		except Exception as e:
			print(e)
	
	def editar_sabor(self, id, nome, valor):
		try:
			sabor = Sabor(emptyToNone(nome), emptyToNone(valor))
			sabor.id = id
			self.saborService.editar(sabor)
		except Exception as e:
			print(e)
	
	def excluir_sabor(self, id):
		try:
			sabor = self.saborService.procurarPorId(id)

			if not sabor:
				raise Exception("Sabor não existe")
			
			self.saborService.excluir(sabor)
		except Exception as e:
			print(e)

	def listar_sabores(self):
		try:
			sabores = self.saborService.listar()
			return sabores
		except Exception as e:
			print(e)