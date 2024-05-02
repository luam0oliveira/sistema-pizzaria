# from Cliente import Cliente
# from Complemento import Complemento
# from Funcionario import Funcionario
# from Sabor import Sabor
# from Usuario import Usuario


# class Menu:
# 	def __init__(self):
# 		self.dados = Banco
# 		self.usuarios: dict[Usuario] = {}
# 		self.complementos: list[Complemento] = []
# 		self.sabores: list[Sabor] = []
# 		self.usuario = None
# 		self.running = True
# 		self.__run()


# 	def __run(self):
# 		while (self.running):
# 			print("Bem vindo à pizzaria AHAHAHDS:")
			
# 			self.__identificacao()

			
# 			if (issubclass)
			
	
# 	def __opcoes_principais(self):
# 		pass

# 	def __identificacao(self):
# 		print("Identificação:\n1 - Login\n2 - Registro\n0 - Sair do sistema")
		
# 		while(True):

# 			op = int(input())

# 			match op:
# 				case 1:
# 					self.__login()
# 					break
# 				case 2:
# 					self.__registro()
# 					break
# 				case 0:
# 					self.__parar()
# 					break
# 				case _:
# 					print("Ação não identificada")

# 	def __parar(self):
# 		self.running = False
		
# 	def __login(self):
# 		login = input("Digite seu cpf: ")
# 		senha = input("Digite sua senha: ")

# 		try:

# 			usuario = self.usuarios.get(login)
# 			if not isinstance(usuario, Usuario):
# 				raise Exception()

# 			if not usuario.login(senha):
# 				raise Exception()

# 			self.usuario = usuario
# 		except:
# 			print("Combinação não encontrada em nosso sistema.")
	
# 	def __registro(self):
# 		# armazena os dados comum a cliente e funcionario
# 		nome = input("Digite seu nome: ")
# 		cpf = input("Digite seu cpf: ")
# 		telefone = input("Digite seu telefone: ")
# 		senha = input("Digite sua senha: ")

# 		if not isinstance(self.usuario, Funcionario):
# 			pessoa = Cliente(nome, cpf, telefone, senha)
# 			self.usuario = pessoa
# 		else:
# 			salario = float(input("Digite o salário do novo funcionário: "))
# 			pessoa = Funcionario(nome, cpf, telefone, senha, salario)
		
# 		self.usuarios[cpf] = pessoa
		
