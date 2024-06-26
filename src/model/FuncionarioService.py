from model.Banco import Banco
from model.Funcionario import Funcionario


class FuncionarioService:
	def __init__(self, banco: Banco):
		self.banco = banco

	def login(self, login, senha):
		funcionario = self.procurarPorCpf(login)
		if not (isinstance(funcionario, Funcionario)):
			raise Exception()
		
		if not funcionario.login(senha):
			raise Exception()

		self.banco.usuario = funcionario
		
		return True
	
	def listar(self):
		funcionarios = self.banco.funcionarios

		return funcionarios

	def procurarPorCpf(self, cpf: str):
		try:
			funcionario = self.banco.funcionarios[cpf]
			return funcionario
		except:
			print("Funcionário não encontrado")

	def criar(self, funcionario: Funcionario):
		try:
			self.banco.funcionarios[funcionario.getCpf()] = funcionario
			print("Funcionario cadastrado com sucesso.")
		except:
			print("CPF já foi utilizado.")
	
	def excluir(self, funcionario: Funcionario):
		try:
			self.banco.funcionarios.pop(funcionario.getCpf())
			print("Funcionario excluído com sucesso.")
		except:
			print("Funcionario não encontrado.")
	
	def editar(self, funcionario: Funcionario):
		try:
			antigo = self.procurarPorCpf(funcionario.getCpf())
			if not antigo:
				raise Exception("Funcionario não encontrado.")
			
			if funcionario.getNome():
				self.banco.funcionarios[funcionario.getCpf()].setNome(funcionario.getNome())

			if funcionario.getSalario():
				self.banco.funcionarios[funcionario.getCpf()].setSalario(funcionario.getSalario())

			if funcionario.getTelefone():
				self.banco.funcionarios[funcionario.getCpf()].setTelefone(funcionario.getTelefone())
			
			if funcionario.getSalario():
				self.banco.funcionarios[funcionario.getCpf()].setTelefone(funcionario.getTelefone())
			
			print("Informações atualizadas.")
		except Exception as e:
			print(e)