from model.Banco import Banco
from model.Complemento import Complemento


class ComplementoService:
	def __init__(self, banco: Banco):
		self.banco = banco

	def procurarPorId(self, id: str):
		try:
			complemento = self.banco.complementos[id]
			return complemento
		except Exception as e:
			print(e)


	def listar(self):
		return self.banco.complementos

	def criar(self, complemento: Complemento):
		self.banco.complementos[complemento.getId()] = complemento

	def excluir(self, complemento: Complemento):
		try:
			self.banco.complementos.pop(complemento.getId())
			print("Complemento excluido")
		except:
			print("Complemento não encontrado.")
	
	def editar(self, complemento: Complemento):
		try:
			if not self.procurarPorId(complemento.getId()):
				raise Exception("Complemento não encontrado.")
			
			self.banco.complementos[complemento.getId()] = complemento
		except Exception as error:
			print(error)