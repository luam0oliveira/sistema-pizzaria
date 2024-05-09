from Banco import Banco
from Cliente import Cliente
from Funcionario import Funcionario
from Sabor import Sabor
from utils import clear_console, delay


class MenuOperacoes:
	def __init__(self, banco: Banco):
		self.running = True
		self.banco = banco
		self.usuario = self.banco.usuario

		if (isinstance(self.usuario, Funcionario)):
			self.__runFuncionario()
		else:
			self.__runCliente()

	def __runFuncionario(self):
		while (self.running):
			print("=== Menu de ações ===")
			print("1 - Adicionar funcionário\n2 - Editar funcionário\n3 - Excluir funcionário\n4 - Listar funcionários")
			print("5 - Adicionar sabor\n6 - Editar sabor\n7 - Excluir sabor\n8 - Listar sabores")
			print("9 - Adicionar complemento\n10 - Editar complemento\n11 - Excluir complemento\n12 - Listar complementos\n0 - Deslogar")
			
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
						self.__criar_complemento()
					case 10:
						self.__editar_complemento()
					case 11:
						self.__excluir_complemento()
					case 12:
						self.__listar_complementos()
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
		
		funcionario = Funcionario(str(self.banco.createFuncionarioId()), nome, cpf, telefone, senha, salario)
		self.banco.adicionarFuncionario(funcionario)
		print("Funcionario cadastrado com sucesso.")
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
			funcionario = self.banco.getFuncionarioPorCpf(cpf)

			nome = input("Digite o nome: ")
			if nome != "":
				funcionario.setNome(nome)
			
			telefone = input("Digite o telefone: ")
			if telefone != "":
				funcionario.setTelefone(telefone)
			salario = float(input("Digite o salário: "))
			if salario >= 0:
				funcionario.setSalario(salario)
		except ValueError:
			salario = ""
			delay(1.5)
			clear_console()
		except Exception as e:
			print(e)
			delay(1.5)
			clear_console()
			return

		self.banco.editarFuncionario(funcionario)
		print("Funcionário editado com sucesso")

		delay(1.5)
		clear_console()

	def __excluir_funcionario(self):
		while(True):
			cpf = input("Digite o cpf: ")
			if cpf != "":
				break
			print("É necessário que preencha o cpf do funcionario")
		
		try:
			funcionario = self.banco.getFuncionarioPorCpf(cpf)

			self.banco.removerFuncionario(funcionario)
			print("Funcionário excluido.")
		except Exception as e:
			print(e)
			delay(1.5)
			clear_console()
			return
	
	def __listar_funcionarios(self):
		clear_console()
		print("=== FUNCIONARIOS ===")
		funcionarios = self.banco.getFuncionarios()
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
			sabor = Sabor(self.banco.createSaborId(), nome, valor)
			self.banco.adicionarSabor(sabor)
		except:
			print("Não foi possivel adicionar o sabor.")
			delay(1.5)

	def __editar_sabor(self):
		try:
			while (True):
				id = input("Digite o id do sabor: ")

				if id != "":
					break
				print("Por favor informe um id valido.")
			
			sabor = self.banco.getSaborPorId(id)

			nome = input("Digite o nome do sabor: ")
			
			if nome != "":
				sabor.nome = nome

			while(True):
				try:
					valor = float(input("Digite o valor do sabor(o valor final da pizza será esse valor * diametro): "))
					if valor > 0:
						break
				except ValueError:
					print("Valor inválido. Digite novamente.")
			
			sabor.valor = valor

			self.banco.editarSabor(sabor)
		except ValueError:
			print("!!")

		except Exception as e:
			print(e)
			delay(1.5)
			clear_console()
			return

	def __excluir_sabor(self):
		try:
			id = input("Digite o id do sabor:")
			self.controller.excluir_sabor(id)
		except:
			print("!!!")
	
	def __listar_sabores(self):
		clear_console()
		print("=== SABORES ===")
		sabores = self.banco.getSabores()
		for i in sabores:
			print(sabores[i])
			print("-----------------------")

	def __listar_complementos(self):
		
		print("=== COMPLEMENTOS ===")
		complementos = self.controller.listar_complementos()
		for i in complementos:
			print(i)
			print(complementos[i])
			print("-----------------------")

	def __criar_complemento(self):
		try:
			nome = input("Digite o nome do complemento: ")
			
			while(True):
				try:
					valor = float(input("Digite o valor do complemento: "))
					if valor > 0:
						break
				except:
					print("Valor inválido. Digite novamente.")
			
			self.controller.adicionar_complemento(nome, valor)
		except:
			print("!!")

	def __editar_complemento(self):
		try:
			id = input("Digite o id do complemento: ")

			nome = input("Digite o nome do complemento: ")

			while(True):
				try:
					valor = float(input("Digite o valor do complemento: "))
					if valor > 0:
						break
				except ValueError:
					print("Valor inválido. Digite novamente.")
			self.controller.editar_complemento(id, nome, valor)
		except ValueError:
			print("!!")

	def __excluir_complemento(self):
		try:
			id = input("Digite o id do complemento:")
			self.controller.excluir_complemento(id)
		except:
			print("!!!")

	# Caso o usuario seja um cliente
	def __runCliente(self):
		while (self.running):
			clear_console()
			print("=== Menu de ações ===")
			print("1 - Fazer pedido\n2 - Confirmar pedido\n3 - Listar pedidos pendentes\n4 - Listar pedidos concluídos\n0 - Deslogar")
			
			try:
				op = int(input())
				match op:
					case 1:
						self.__fazer_pedido()
					case 2:
						self.__confirmar_pedido()
					case 3:
						clear_console()
						self.__listar_pedidos_pendentes()
						input("Aperte enter para prosseguir...")
					case 4:
						clear_console()
						self.__listar_pedidos_concluidos()
						input("Aperte enter para prosseguir...")
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
	
	def __listar_pedidos_pendentes(self):
		print("==== PENDENTES ====")
		if isinstance(self.usuario, Cliente):
			for i in self.usuario.pedidos:
				if not self.usuario.pedidos[i].entregue: print(str(self.usuario.pedidos[i]) + "\n--------------------")
		
	def __listar_pedidos_concluidos(self):
		print("==== CONCLUIDOS ====")
		if isinstance(self.usuario, Cliente):
			for i in self.usuario.pedidos:
				if self.usuario.pedidos[i].entregue: print(str(self.usuario.pedidos[i]) + "\n--------------------")

	def __confirmar_pedido(self):
		try:
			id = input("Digite o id do seu pedido: ")

			if  id not in self.usuario.pedidos:
				raise Exception("")
			self.usuario.pedidos[id].entregue = True
		except:
			print("pedido não encontrado.")
		

	def __fazer_pedido(self):
		self.controller.fazer_pedido(self.usuario)