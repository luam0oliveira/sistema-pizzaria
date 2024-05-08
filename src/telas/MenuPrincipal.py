from Banco import Banco
from utils import clear_console, delay
from telas.MenuLogin import MenuLogin


class MenuPrincipal:
	def __init__(self):
		self.running = True
		self.banco = Banco()
		self.run()

	def run(self):
		clear_console()

		while (self.running):
			print("=== Bem vindo a pizzaria AHHAHASHDU! ===")
			try: 

				# autenticacao e registro de usuario
				self.login()
				
				if not self.banco.usuario: return
				else: print(self.banco.usuario)
				delay(5)

				self.operacoes()
				clear_console()
			except KeyboardInterrupt:
				break
	
	def login(self):
		MenuLogin(self.banco)
	

	def operacoes(self):
		pass
	

			
	

	