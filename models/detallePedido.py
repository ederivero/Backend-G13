from utilitarios import conexion
from sqlalchemy import Column, types, ForeignKey

class DetallePedidoModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    cantidad = Column(type_=types.Integer, nullable=False)
    precio = Column(type_=types.Float, nullable=False)
    subTotal = Column(type_=types.Float, nullable=False)
    productoId = Column(ForeignKey('productos.id'), type_=types.Integer, nullable=False, 
                        name='producto_id')
    pedidoId = Column(ForeignKey('pedidos.id'), type_=types.Integer, nullable=False,
                      name='pedido_id')
    
    __tablename__ ='detalle_pedidos'
