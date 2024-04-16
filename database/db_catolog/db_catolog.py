from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class catolog(base):
    __tablename__ = 'catolog'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    product_type = Column(Integer, ForeignKey('product_type.id'))
    description = Column(String(2555), nullable=False, default="Отсутвует")
    price = Column(Double, nullable=False, default=0.0)
    type_realt = relationship("product_type", uselist=False, back_populates="product_type_realt")
    # cart_realt = relationship("cart")