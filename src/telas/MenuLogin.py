from logging import raiseExceptions
from Cliente import Cliente
from utils import clear_console, delay


class MenuLogin:
	def __init__(self, banco):
		self.running = True
		self.banco = banco
		self.__run()

	def __run(self):

		while (self.running):
			print("Autenticação:\n1 - Login como cliente\n2 - Login como funcionário\n3 - Registro de cliente\n0 - Sair")
			try:
				op = int(input())
				match op:
					case 1:
						self.__login_cliente()
					case 2:
						self.__login_funcionario()
					case 3:
						self.__registro_cliente()
					case 0:
						self.__deslogar()
						return
					case _:
						raise Exception("Entrada invalida")
			except KeyboardInterrupt:
				clear_console()
				print("Cancelando operação e voltando para o menu de login.")
			except ValueError:
				clear_console()
				print("Entrada inválida.")
			except Exception as e:
				print(e)
			delay(1.5)
			clear_console()

	def __login_cliente(self):
		clear_console()
		print("==== Login de cliente ====")
		cpf = input("Digite seu cpf: ")
		senha = input("Digite sua senha: ")
		
		# Verifica se o usuario existe
		if (not self.banco.clientes.get(cpf)):
			raise Exception("Usuario não encontrado.")
			
		
		self.running = not self.banco.clientes[cpf].login(senha)
		if (self.running):
			raise Exception("Combinacao cpf senha não encontrado.")
		print("Cliente autenticado.")
		self.banco.usuario = self.banco.clientes[cpf]

	def __registro_cliente(self):
		clear_console()
		print("==== Registro de cliente ====")
		nome = input("Digite seu nome: ")
		telefone = input("Digite seu telefone: ")
		cpf = input("Digite seu cpf: ")
		senha = input("Digite sua senha: ")
		
		# impede que existam dois clientes com o mesmo cpf
		if (self.banco.cliente.get(cpf)):
			raise Exception("CPF já esta em uso.")

		for i in [nome,telefone,cpf,senha]:
			if i.strip() == "":
				raise Exception("É necessário que todos os dados sejam preenchidos.")

		cliente = Cliente(nome, cpf, telefone, senha)

		self.banco.cliente[cpf] = cliente
		print("Cliente cadastrado com sucesso.")

	def __login_funcionario(self):
		clear_console()
		print("==== Login de funcionario ====")
		cpf = input("Digite seu cpf: ")
		senha = input("Digite sua senha: ")
		
		# Verifica se o funcionario existe
		if (not self.banco.funcionarios.get(cpf)):
			raise Exception("Funcionario não encontrado.")
			
		self.running = not self.banco.funcionarios[cpf].login(senha)

		if (self.running):
			raise Exception("Combinacao cpf senha não encontrado.")
		self.banco.usuario = self.banco.funcionarios[cpf]
		print("Funcionario autenticado.")
	
	def __deslogar(self):
		self.banco.usuario = None
