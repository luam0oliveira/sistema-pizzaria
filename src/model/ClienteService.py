from model.Banco import Banco
from model.Cliente import Cliente


class ClienteService:
	def __init__(self, banco: Banco):
		self.banco = banco

	def login(self, login, senha):
		cliente = self.procurarPorCpf(login)
		if not (isinstance(cliente, Cliente)):
			raise Exception()
		
		if not cliente.login(senha):
			raise Exception()

		self.banco.usuario = cliente
		
		return True
			

	def procurarPorCpf(self, cpf: str):
		try:
			cliente = self.banco.clientes.get(cpf)

			print(cliente)
			return cliente
		except Exception as e:
			print(e)

	def criar(self, cliente: Cliente):
		try:
			self.banco.clientes[cliente.getCpf()] = cliente
			print("Cliente cadastrado com sucesso.")
		except:
			print("CPF já foi utilizado.")
	
	def excluir(self, cliente: Cliente):
		try:
			self.banco.clientes.pop(cliente.getCpf())
			print("Cliente excluído com sucesso.")
		except:
			print("Cliente não encontrado.")
	
	def editar(self, cliente: Cliente):
		try:
			self.banco.clientes[cliente.getCpf()] = cliente
			print("Cliente cadastrado com sucesso.")
		except:
			print("CPF já foi utilizado.")