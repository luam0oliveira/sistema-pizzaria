from uuid import uuid4
from model.Complemento import Complemento
from model.Endereco import Endereco
from Pizza import Pizza


class Pedidos:
	def __init__(self, endereco: Endereco):
		self.__id = uuid4()
		self.__endereco = endereco
		self.__pizzas:list[Pizza] = []
		self.__complementos:list[Complemento] = []
	

	def adicionarPizza(self, pizza: Pizza):
		self.__pizzas.append(pizza)

	def adicionarComplemento(self, complemento: Complemento):
		self.__complementos.append(complemento)
	
	def calculaValor(self):
		valor = 0

		for pizza in self.__pizzas:
			valor += pizza.calculaPreco()

		for complemento in self.__complementos:
			valor += complemento.getValor()
		
		return valor
