from Cliente import Cliente
from Complemento import Complemento
from Funcionario import Funcionario
from Pedido import Pedido
from Sabor import Sabor


class Banco:
	def __init__(self):
		self.clientes = {'1': Cliente('0',"dmt", '1', "123", '1')}
		self.funcionarios = {'0': Funcionario('0',"adm", '0', '0', '0', 100)}
		self.sabores = {'1': Sabor('1', "Cala,bresa", 5 ), '2': Sabor('2', "Calafrango", 7), '3': Sabor('3', "TacumFome", 10)}
		self.complementos = {'1': Complemento('1', "TacumSede", 10), '2':Complemento('2', "Água", 8)}
		self.usuario = None
		
		self.clienteId = 1
		self.funcionarioId = 1
		self.saborId = 4
		self.complementoId = 3
		self.pedidoId = 1
	
	def createClienteId(self):
		return str(self.clienteId)

	def createFuncionarioId(self):
		return str(self.funcionarioId)

	def createSaborId(self):
		return str(self.saborId)

	def createComplementoId(self):
		return str(self.complementoId)

	def createPedidoId(self):
		return str(self.pedidoId)
	
	def incrementClienteId(self):
		self.clienteId+=1
	
	def incrementFuncionarioId(self):
		self.funcionarioId += 1

	def incrementSaborId(self):
		self.saborId += 1
	
	def incrementComplementoId(self):
		self.complementoId += 1

	def incrementPedidoId(self):
		self.pedidoId += 1
	
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
	
	# metodos relacionados a sabor
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
	
	def removerSabor(self, sabor: Sabor):
		self.sabores.pop(sabor.id)

	# metodos relacionados a complementos
	def getComplementoPorId(self, id: str):
		complemento = self.complementos.get(id)
		if not complemento:
			raise Exception("Complemento não encontrado.")
		return complemento

	def getComplementos(self):
		return self.complementos

	def adicionarComplemento(self, complemento: Complemento):
		self.complementos[complemento.getId()] = complemento
		self.incrementComplementoId()
	
	def editarComplemento(self, complemento: Complemento):
		self.complementos[complemento.getId()] = complemento

	def removerComplemento(self, complemento: Complemento):
		self.complementos.pop(complemento.getId())
	
	def adicionarCliente(self, cliente: Cliente):
		self.clientes[cliente.getId()] = cliente
		self.incrementClienteId()
	
	def finalizar_pedido(self, pedido: Pedido):
		try:
			if isinstance(self.usuario, Cliente) and len(pedido.pizzas) != 0:
				self.usuario.pedidos[pedido.id] = pedido
				self.incrementPedidoId()
				return True
			return False
		except Exception as e:
			return False
	
	
