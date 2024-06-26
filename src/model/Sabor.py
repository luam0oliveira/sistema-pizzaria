from uuid import uuid4


class Sabor:
	def __init__(self, nome: str, valor: float, id = str(uuid4()),):
		self.id = id
		self.nome = nome
		self.valor = valor
	
	def __str__(self) -> str:
		return f"id = {self.id}\tnome = {self.nome}\tvalor = {self.valor}"