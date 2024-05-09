from Pedido import Pedido
from Usuario import Usuario


class Cliente(Usuario):
	def __init__(self, id = int, nome: str = None, cpf: str = None, telefone: str = None, senha: str = None):
		super().__init__(id, nome, cpf, telefone, senha)
		self.pedidos:dict[Pedido] = {}

	def __str__(self) -> str:
		return f"cpf: {self.getCpf()}"
