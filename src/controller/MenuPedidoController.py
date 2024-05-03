from model.ClienteService import ClienteService
from model.ComplementoService import ComplementoService
from model.SaborService import SaborService


class MenuPedidoController:
	def __init__(self, clienteService: ClienteService,
			saborService: SaborService = None,
			complementoService: ComplementoService = None):
		self.clienteService = clienteService
		self.saborService = saborService
		self.complementoService = complementoService
	

	def listar_sabores(self):
		return self.saborService.listar()

	def listar_complementos(self):
		return self.complementoService.listar()

	def fazer_pedido(self):
		pass