from model.Usuario import Usuario


class Cliente(Usuario):
	def __init__(self, nome: str = None, cpf: str = None, telefone: str = None, senha: str = None):
		super().__init__(nome, cpf, telefone, senha)

	def __str__(self) -> str:
		return f"cpf: {self.getCpf()}"
