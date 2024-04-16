from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class product_type(base):
    __tablename__ = 'product_type'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("catolog.id"))
    image_path = Column(String(528), nullable=False)
    product_realt = relationship("catolog")
