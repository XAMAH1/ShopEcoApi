from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class cart(base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('catolog.id'))
    user_id = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False, default=1)
