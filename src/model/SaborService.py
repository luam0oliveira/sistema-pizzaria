from model.Banco import Banco
from model.Sabor import Sabor


class SaborService:
	def __init__(self, banco: Banco):
		self.banco = banco

	def listar(self):
		try:
			sabores = self.banco.sabores
			return sabores
		except:
			print("!!!")

	def procurarPorId(self, id: str):
		try:
			sabor = self.banco.sabores[id]
			return sabor
		except:
			print("Sabor não encontrado")

	def criar(self, sabor: Sabor):
		try:
			self.banco.sabores[sabor.id] = sabor
			print("Sabor cadastrado com sucesso.")
		except:
			print("CPF já foi utilizado.")
	
	def excluir(self, sabor: Sabor):
		try:
			self.banco.sabores.pop(sabor.id)
			print("Sabor excluído com sucesso.")
		except:
			print("Sabor não encontrado.")
	
	def editar(self, sabor: Sabor):
		try:
			if not self.procurarPorId(sabor.id):
				raise Exception("Sabor não encontrado.")

			self.banco.sabores[sabor.id] = sabor
			print("Informações atualizadas.")
		except Exception as e:
			print(e)