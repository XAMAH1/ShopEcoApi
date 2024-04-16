from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class catolog_image(base):
    __tablename__ = 'catolog_image'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("catolog.id"))
    image_path = Column(String(528), nullable=False)
    product_realt = relationship("catolog")
