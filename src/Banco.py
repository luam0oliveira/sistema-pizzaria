from Cliente import Cliente
from Complemento import Complemento
from Funcionario import Funcionario
from Sabor import Sabor


class Banco:
	def __init__(self):
		self.clientes = {'1': Cliente(0,"dmt", '1', "123", '1')}
		self.funcionarios = {'0': Funcionario(0,"adm", '0', '0', '0', 100)}
		self.sabores = {'1': Sabor("Cala,bresa", 5, '1'), '2': Sabor("Calafrango", 7, '2'), '3': Sabor("TacumFome", 10, '3')}
		self.complementos = {'1': Complemento("TacumSede", 10, '1'), '2':Complemento("Água", 8, '2')}
		self.usuario = None
		
		self.clienteId = 1
		self.funcionarioId = 1
	
	def createClienteId(self):
		return self.clienteId

	def createFuncionarioId(self):
		return self.funcionarioId

	def incrementClienteId(self):
		self.clienteId+=1
	
	def incrementFuncionarioId(self):
		self.funcionarioId += 1

	def getFuncionarioPorCpf(self, cpf:str) -> Funcionario:
		funcionario = self.funcionarios.get(cpf)
		if not funcionario:
			raise Exception("Funcionario não encontrado")
		return funcionario

	def adicionarFuncionario(self, funcionario: Funcionario):
		self.funcionarios[funcionario.getId()] = funcionario
		self.incrementFuncionarioId()
	
	def editarFuncionario(self, funcionario:Funcionario):
		self.funcionarios[funcionario.getId()] = funcionario
		print(self.funcionarios[funcionario.getId()])
	
	def removerFuncionario(self, funcionario: Funcionario):
		self.funcionarios.pop(funcionario.getId())
	
	def adicionarCliente(self, cliente: Cliente):
		self.clientes[cliente.getId()] = cliente
		self.incrementClienteId()
	
	
