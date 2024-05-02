from controller.MenuLoginController import MenuLoginController


class MenuLogin:
	def __init__(self, funcionarioService, clienteService):
		self.controller = MenuLoginController(funcionarioService, clienteService)
		self.running = True
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
						break
					case _:
						raise Exception("Entrada invalida")
			except KeyboardInterrupt:
				break
			except Exception as e:
				print(e)


	def __login_cliente(self):
		cpf = input("Digite seu cpf: ")
		senha = input("Digite sua senha: ")
		
		self.running = not self.controller.login_cliente(cpf, senha)

	def __registro_cliente(self):
		nome = input("Digite seu nome: ")
		telefone = input("Digite seu telefone: ")
		cpf = input("Digite seu cpf: ")
		senha = input("Digite sua senha: ")
		
		self.controller.registro_cliente(nome, cpf, telefone, senha)

	def __login_funcionario(self):
		cpf = input("Digite seu cpf: ")
		senha = input("Digite sua senha: ")
		
		self.running = not self.controller.login_funcionario(cpf, senha)
