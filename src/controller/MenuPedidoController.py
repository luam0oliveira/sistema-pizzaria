from model.Cliente import Cliente
from model.ClienteService import ClienteService
from model.ComplementoService import ComplementoService
from model.Pedido import Pedido
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

	def finalizar(self, pedido:Pedido):
		try:
			if isinstance(self.clienteService.banco.usuario, Cliente) and len(pedido.pizzas) != 0: 
				self.clienteService.banco.usuario.pedidos[pedido.id] = pedido
				return True
			return False
		except Exception as e:
			return False