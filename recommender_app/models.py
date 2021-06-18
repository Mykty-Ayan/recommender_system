from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
metadata = Base.metadata


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(BigInteger, primary_key=True, index=True, server_default=text("nextval('brand_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)


class Category(Base):
    __tablename__ = 'category'

    id = Column(BigInteger, primary_key=True, index=True, server_default=text("nextval('category_id_seq'::regclass)"))
    name = Column(String(1024), nullable=False)


class FlywaySchemaHistory(Base):
    __tablename__ = 'flyway_schema_history'

    installed_rank = Column(Integer, primary_key=True)
    version = Column(String(50))
    description = Column(String(200), nullable=False)
    type = Column(String(20), nullable=False)
    script = Column(String(1000), nullable=False)
    checksum = Column(Integer)
    installed_by = Column(String(100), nullable=False)
    installed_on = Column(DateTime, nullable=False, server_default=text("now()"))
    execution_time = Column(Integer, nullable=False)
    success = Column(Boolean, nullable=False, index=True)


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    address = Column(String(1024))


class Order(Base):
    __tablename__ = 'orders'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('orders_id_seq'::regclass)"))
    user_id = Column(ForeignKey('users.id'), nullable=False, server_default=text("nextval('orders_user_id_seq'::regclass)"))
    order_date = Column(DateTime, server_default=text("timezone('utc'::text, now())"))

    user = relationship('User')


class Product(Base):
    __tablename__ = 'product'

    id = Column(BigInteger, primary_key=True, index=True, server_default=text("nextval('product_id_seq'::regclass)"))
    name = Column(String(2048), nullable=False)
    price = Column(Float(53))
    brand_id = Column(ForeignKey('brand.id'), nullable=False, server_default=text("nextval('product_brand_id_seq'::regclass)"))
    category_id = Column(ForeignKey('category.id'), nullable=False, server_default=text("nextval('product_category_id_seq'::regclass)"))
    description = Column(String(32768))
    image = Column(String(4096))

    brand = relationship('Brand')
    category = relationship('Category')


class OrdersProduct(Base):
    __tablename__ = 'orders_product'

    order_id = Column(ForeignKey('orders.id'), ForeignKey('orders.id'), primary_key=True, nullable=False, server_default=text("nextval('orders_product_order_id_seq'::regclass)"))
    product_id = Column(ForeignKey('product.id'), ForeignKey('product.id'), primary_key=True, nullable=False, server_default=text("nextval('orders_product_product_id_seq'::regclass)"))
    quantity = Column(Integer, nullable=False)

    order = relationship('Order', primaryjoin='OrdersProduct.order_id == Order.id')
    order1 = relationship('Order', primaryjoin='OrdersProduct.order_id == Order.id')
    product = relationship('Product', primaryjoin='OrdersProduct.product_id == Product.id')
    product1 = relationship('Product', primaryjoin='OrdersProduct.product_id == Product.id')
