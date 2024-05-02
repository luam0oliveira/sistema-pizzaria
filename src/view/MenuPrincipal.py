from controller.MenuPrincipalController import MenuPrincipalController
from utils import clear_console, delay


class MenuPrincipal:
	def __init__(self):
		self.controller = MenuPrincipalController()
		self.running = True
		self.run()

	def run(self):
		clear_console()
		print("=== Bem vindo a pizzaria AHHAHASHDU! ===")

		while (self.running):
			# autenticacao e registro de usuario 
			self.controller.login()
			
			if not self.controller.banco.usuario: return

			self.running = self.controller.operacoes()




			
	

	