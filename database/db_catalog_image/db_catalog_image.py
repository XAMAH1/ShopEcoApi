from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class catalog_image(base):
    __tablename__ = 'catalog_image'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("catalog.id"))
    image_path = Column(String(528), nullable=False)
    product_realt = relationship("catalog")
