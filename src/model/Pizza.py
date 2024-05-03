from uuid import uuid4

from model.Sabor import Sabor


class Pizza:
	def __init__(self, sabor:Sabor, diametro: int):
		self.__id = str(uuid4())
		self.__sabor = sabor
		self.__diametro = diametro
	
	# diametro * sabor
	def getId(self):
		return self.__id
	
	def calculaPreco(self):
		return self.__diamatro * self.__sabor.valor

	def getSabor(self):
		return self.__sabor
	
	def setSabor(self, sabor:Sabor):
		self.__sabor = sabor
	
	def getDiametro(self):
		return self.__diametro

	def setDiametro(self, diametro:int):
		self.__diametro = diametro
