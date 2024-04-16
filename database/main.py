from sqlalchemy import *
from sqlalchemy import exc as sa_exc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import warnings

from config import BASE_CONFIG
from database.base import base

from database.db_cart.db_cart import *
from database.db_catolog.db_catolog import *
from database.db_product_type.db_product_type import *
from database.db_catolog_image.db_catolog_image import *


warnings.filterwarnings('ignore', category=sa_exc.SAWarning)


timeout = 10
engine = create_engine(f'mysql+pymysql://{BASE_CONFIG["BASE_USER"]}:{BASE_CONFIG["BASE_PASSWORD"]}@{BASE_CONFIG["BASE_HOST"]}/{BASE_CONFIG["BASE_TABLE"]}', connect_args={'connect_timeout': timeout})


base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
