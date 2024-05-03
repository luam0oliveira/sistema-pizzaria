class Endereco:
	def __init__(self, rua: str, numero: str, bairro: str, complemento: str, cidade: str, estado: str, cep: str):
		self.rua = rua
		self.numero = numero
		self.bairro = bairro
		self.complemento = complemento
		self.cidade = cidade
		self.estado = estado
		self.cep = cep
	
	def __str__(self) -> str:
		return f"rua: {self.rua}\tnumero: {self.numero}"
		