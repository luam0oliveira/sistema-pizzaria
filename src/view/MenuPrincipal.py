from controller.MenuPrincipalController import MenuPrincipalController
from view.MenuLogin import MenuLogin


class MenuPrincipal:
	def __init__(self):
		self.controller = MenuPrincipalController()
		self.run()

	def run(self):
		print("=== Bem vindo a pizzaria AHHAHASHDU! ===")

		while (True):
			self.controller.login()
			return
	

	