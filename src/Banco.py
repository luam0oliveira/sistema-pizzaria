from Cliente import Cliente
from Complemento import Complemento
from Funcionario import Funcionario
from Sabor import Sabor


class Banco:
	def __init__(self):
		self.clientes = {'1': Cliente('0',"dmt", '1', "123", '1')}
		self.funcionarios = {'0': Funcionario('0',"adm", '0', '0', '0', 100)}
		self.sabores = {'1': Sabor('1', "Cala,bresa", 5 ), '2': Sabor('2', "Calafrango", 7), '3': Sabor('3', "TacumFome", 10)}
		self.complementos = {'1': Complemento("TacumSede", 10, '1'), '2':Complemento("Água", 8, '2')}
		self.usuario = None
		
		self.clienteId = 1
		self.funcionarioId = 1
		self.saborId = 4
		self.complementoId = 3
	
	def createClienteId(self):
		return str(self.clienteId)

	def createFuncionarioId(self):
		return str(self.funcionarioId)

	def createSaborId(self):
		return str(self.saborId)

	def createComplementoId(self):
		return str(self.complementoId)

	def incrementClienteId(self):
		self.clienteId+=1
	
	def incrementFuncionarioId(self):
		self.funcionarioId += 1

	def incrementSaborId(self):
		self.saborId += 1
	
	def incrementComplementoId(self):
		self.complementoId += 1

	# metodos relacionadas a funcionario
	def getFuncionarioPorCpf(self, cpf:str) -> Funcionario:
		funcionario = self.funcionarios.get(cpf)
		if not funcionario:
			raise Exception("Funcionario não encontrado")
		return funcionario

	def getFuncionarios(self) -> list[Funcionario]:
		return self.funcionarios

	def adicionarFuncionario(self, funcionario: Funcionario):
		self.funcionarios[funcionario.getCpf()] = funcionario
		self.incrementFuncionarioId()
	
	def editarFuncionario(self, funcionario:Funcionario):
		self.funcionarios[funcionario.getCpf()] = funcionario
	
	def removerFuncionario(self, funcionario: Funcionario):
		self.funcionarios.pop(funcionario.getCpf())
	
	# metodos relacionados ao sabor
	def getSaborPorId(self, id: str):
		sabor = self.sabores.get(id)

		if not sabor:
			raise Exception("Não existe sabor com esse id.")
		return sabor
	
	def getSabores(self):
		return self.sabores
	
	def adicionarSabor(self, sabor: Sabor):
		self.sabores[sabor.id] = sabor

		self.incrementSaborId()

	def editarSabor(self, sabor: Sabor):
		self.sabores[sabor.id] = sabor



	def adicionarCliente(self, cliente: Cliente):
		self.clientes[cliente.getId()] = cliente
		self.incrementClienteId()
	
	
