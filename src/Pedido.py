from uuid import uuid4

from model.Complemento import Complemento
from model.Pizza import Pizza


class Pedido:
	def __init__(self, usuario_id: str):
		self.id = str(uuid4())
		self.usuario_id = usuario_id
		self.endereco = None
		self.pizzas:list[Pizza] = []
		self.complementos:list[Complemento] = []
		self.entregue = False
	
	def adicionar_pizza(self, pizza):
		self.pizzas.append(pizza)

	def adicionar_complemento(self, complemento):
		self.complementos.append(complemento)
	
	def calculaTotal(self):
		valor = 0

		for i in self.pizzas:
			valor += i.calculaPreco()

		for i in self.complementos:
			valor += i.getValor()
		
		return valor

	def __str__(self) -> str:
		return f"Id de pedido: {self.id}\nEndereco:{self.endereco}\nTotal: {self.calculaTotal()}"
