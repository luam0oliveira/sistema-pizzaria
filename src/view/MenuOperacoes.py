from controller.MenuOperacoesController import MenuOperacoesController
from model.ClienteService import ClienteService
from model.ComplementoService import ComplementoService
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
			print("1 - Adicionar funcionário\n2 - Editar funcionário\n3 - Excluir funcionário")
			print("4 - Adicionar sabor\n5 - Editar sabor\n6 - Excluir sabor")
			print("7 - Adicionar complemento\n8 - Editar complemento\n9 - Excluir complemento\n0 - Deslogar")
			
			try:
				op = int(input())
				match op:
					case 1:
						self.__adicionar_funcionario()
					case 2:
						self.__editar_funcionario()
					case 3:
						pass
					case 4:
						pass
					case 5:
						pass
					case 6:
						pass
					case 7:
						pass
					case 8:
						pass
					case 9:
						pass
					case 0:
						pass					
					case _:
						raise Exception("Entrada invalida")
			except KeyboardInterrupt:
				break
			except Exception as e:
				print(e)
			
	def __adicionar_funcionario(self):
		try:
			print("\n\nAperte Control-C para cancelar a operação")
			nome = input("Digite seu nome: ")
			telefone = input("Digite seu telefone: ")
			cpf = input("Digite seu cpf: ")
			senha = input("Digite sua senha: ")
			salario = float(input("Digite o salário: "))
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
		except KeyboardInterrupt:
			clear_console()
			print("Cancelando alterações e voltando para menu de operações")
			delay(2)
			clear_console()
			return
		self.controller.editar_funcionario(nome, cpf, telefone, salario)

		delay(1.5)
		clear_console()

	
	def __runCliente(self):
		pass