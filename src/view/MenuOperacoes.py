from controller.MenuOperacoesController import MenuOperacoesController
from model.ClienteService import ClienteService
from model.ComplementoService import ComplementoService
from model.Funcionario import Funcionario
from model.FuncionarioService import FuncionarioService
from model.SaborService import SaborService
from utils import clear_console, delay


class MenuOperacoes:
	def __init__(self,
			  ehFuncionario,
			  clienteService: ClienteService,
			  funcionarioService:FuncionarioService = None,
			  saborService: SaborService = None,
			  complementoService: ComplementoService = None):
		self.running = True
		self.controller = MenuOperacoesController(clienteService, funcionarioService, saborService, complementoService)

		if (ehFuncionario):
			self.__runFuncionario()
		else:
			self.__runCliente()

	def __runFuncionario(self):
		while (self.running):
			print("=== Menu de ações ===")
			print("1 - Adicionar funcionário\n2 - Editar funcionário\n3 - Excluir funcionário\n4 - Listar funcionários")
			print("5 - Adicionar sabor\n6 - Editar sabor\n7 - Excluir sabor\n8 - Listar sabores")
			print("7 - Adicionar complemento\n8 - Editar complemento\n9 - Excluir complemento\n0 - Deslogar")
			
			try:
				op = int(input())
				match op:
					case 1:
						self.__adicionar_funcionario()
					case 2:
						self.__editar_funcionario()
					case 3:
						self.__excluir_funcionario()
					case 4:
						self.__listar_funcionarios()
					case 5:
						self.__adicionar_sabor()
					case 6:
						self.__editar_sabor()
					case 7:
						self.__excluir_sabor()
					case 8:
						self.__listar_sabores()
					case 9:
						pass
					case 0:
						clear_console()
						return False					
					case _:
						raise Exception("Entrada invalida")
			except KeyboardInterrupt:
				clear_console()
				print("Cancelando operação e voltando para o menu de login.")
				delay(1.5)
				clear_console()
			except Exception as e:
				print(e)
			
	def __adicionar_funcionario(self):
		try:
			print("\n\nAperte Control-C para cancelar a operação")
			nome = input("Digite seu nome: ")
			telefone = input("Digite seu telefone: ")
			cpf = input("Digite seu cpf: ")
			senha = input("Digite sua senha: ")
			while (True):
				salario = float(input("Digite o salário: "))
				if salario > 0:
					break
		except ValueError:
			print("Entrada incorreta, voltando para o menu de operações")
			delay(1.5)
			clear_console()
		except KeyboardInterrupt:
			clear_console()
			print("Cancelando alterações e voltando para menu de operações")
			delay(2)
			clear_console()
			return
		self.controller.adicionar_funcionario(nome, cpf, telefone, senha, salario)

		delay(1.5)
		clear_console()

	def __editar_funcionario(self):
		try:
			print("\n\nAperte Control-C para cancelar a operação")
			print("Caso não queria mudar algum campo, não digite nada e aperte Enter")
			while(True):
				cpf = input("Digite o cpf: ")
				if cpf != "":
					break
				print("É necessário que preencha o cpf do funcionario")
			nome = input("Digite o nome: ")
			telefone = input("Digite o telefone: ")
			salario = float(input("Digite o salário: "))
		except ValueError:
			salario = ""
			delay(1.5)
			clear_console()

		self.controller.editar_funcionario(nome, cpf, telefone, salario)

		delay(1.5)
		clear_console()

	def __excluir_funcionario(self):
		while(True):
			cpf = input("Digite o cpf: ")
			if cpf != "":
				break
			print("É necessário que preencha o cpf do funcionario")
		
		self.controller.excluir_funcionario(cpf)
	
	def __listar_funcionarios(self):
		clear_console()
		print("=== FUNCIONARIOS ===")
		funcionarios = self.controller.listar_funcionarios()
		for i in funcionarios:
			print(funcionarios[i])
			print("-----------------------")

	def __adicionar_sabor(self):
		try:
			nome = input("Digite o nome do sabor: ")
			
			while(True):
				try:
					valor = float(input("Digite o valor do sabor(o valor final da pizza será esse valor * diametro): "))
					if valor > 0:
						break
				except:
					print("Valor inválido. Digite novamente.")
			
			self.controller.adicionar_sabor(nome, valor)
		except:
			print("!!")

	def __editar_sabor(self):
		try:
			id = input("Digite o id do sabor: ")

			nome = input("Digite o nome do sabor: ")

			while(True):
				try:
					valor = input("Digite o valor do sabor(o valor final da pizza será esse valor * diametro): ")
					if valor > 0:
						break
				except ValueError:
					print("Valor inválido. Digite novamente.")
			self.controller.editar_sabor(id, nome, valor)
		except ValueError:
			print("!!")

	def __excluir_sabor(self):
		try:
			id = input("Digite o id do sabor:")
			self.controller.excluir_sabor(id)
		except:
			print("!!!")
	
	def __listar_sabores(self):
		clear_console()
		print("=== SABORES ===")
		sabores = self.controller.listar_sabores()
		for i in sabores:
			print(sabores[i])
			print("-----------------------")


	def __runCliente(self):
		pass