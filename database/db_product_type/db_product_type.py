from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class product_type(base):
    __tablename__ = 'product_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    product_type_realt = relationship("catolog")
