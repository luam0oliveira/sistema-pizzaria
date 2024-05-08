from controller.MenuPedidoController import MenuPedidoController
from model.Endereco import Endereco
from model.Pedido import Pedido
from model.Pizza import Pizza
from model.Usuario import Usuario
from utils import clear_console, delay


class MenuPedido:
	def __init__(self, usuario:Usuario, clienteService, saborService, complementoService):
		self.controller = MenuPedidoController(clienteService, saborService, complementoService)
		self.usuario = usuario
		self.pedido = Pedido(self.usuario.getId())
		self.__run()
	
	def __run(self):
		endereco = self.__pegar_endereco()
		self.pedido.endereco = endereco
		while(True):
			print("=======  PEDIDO  =======")
			print("1 - Adicionar pizza\n2 - Adicionar complemento\n3 - Listar produtos de pedido\n4 - Finalizar\n0 - Cancelar")
			try:
				op = int(input())
				match op:
					case 1:
						self.__adicionar_pizza()
					case 2:
						self.__adicionar_complemento()
					case 3:
						self.__listar_produtos()
					case 4:
						st = self.__finalizar()
						if (st):
							print("Pedido finalizado")
							delay(2)
							clear_console()
							return True
						clear_console()
					case 0:
						clear_console()
						return False					
					case _:
						raise Exception("Entrada invalida")
			except KeyboardInterrupt:
				clear_console()
				print("Cancelando operação e voltando para o menu de pedido.")
				delay(1.5)
				clear_console()
			except Exception as e:
				print(e)

	def __pegar_endereco(self):
		while(True):
			rua = input("Digite sua rua: ")
			numero = input("Digite sua numero: ")
			bairro = input("Digite sua bairro: ")
			complemento = input("Digite sua complemento: ")
			cidade = input("Digite sua cidade: ")
			estado = input("Digite sua estado: ")
			cep = input("Digite sua cep: ")
			if rua != "" and numero != "":
				break
			print("Por favor, coloque o nome da rua e numero.")
		clear_console()
		return Endereco(rua, numero, bairro, complemento, cidade, estado, cep)

	def __adicionar_pizza(self):
		sabores = self.controller.listar_sabores()
		while(True):
			print("SABORES DISPONIVEIS (somente 1): ")
			for i in sabores:
				print(sabores[i])
				print("-------------------------")

			sabor = input("Digite o id do sabor escolhido: ")

			if sabor in sabores:
				break
			print("Sabor desconhecido, por favor digite novamente.")

		while(True):
			try:
				diametro = int(input("Digite o diametro da pizza (maior de 10 cm, só trabalhamos com dimatros inteiros):"))

				if diametro > 10:
					break
				print("Digite um diametro, válido por favor")
			except ValueError:
				print("Valor incorreto, digite novamente.")
		pizza = Pizza(sabores[sabor], diametro)

		self.pedido.adicionar_pizza(pizza)
		print("Pizza adicionada com sucesso.")
		delay(1.5)
		clear_console()

	def __adicionar_complemento(self):
		complementos = self.controller.listar_complementos()
		while(True):
			print("COMPLEMENTOS DISPONIVEIS (somente 1): ")
			for i in complementos:
				print(complementos[i])
				print("-------------------------")

			complemento = input("Digite o id do complemento escolhido: ")

			if complemento in complementos:
				break
			print("Sabor desconhecido, por favor digite novamente.")


		self.pedido.adicionar_complemento(complementos[complemento])
		print("Complemento adicionado com sucesso")
		delay(1.5)
		clear_console()

	def __finalizar(self):
		st = self.controller.finalizar(self.pedido)
		if st:
			print("Pedido finalizado com sucesso. Quando chegar, confirme em nosso sistema, por favor.")
		else:
			print("É necessário que tenha ao menos comprado uma pizza.")
		delay(3)
		clear_console()
		return st

	def __listar_produtos(self):
		print("========== LISTA DE PRODUTOS ===========")
		
		for i in self.pedido.pizzas:
			print(i)
			print("--------------------")
		
		for i in self.pedido.complementos:
			print(i)
		print("--------------------")
	

		
