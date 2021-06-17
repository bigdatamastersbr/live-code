from decimal import Decimal
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date
from SessionConfig import *
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Numeric

class Customer(Base):
    
    __tablename__ = 'Customer'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    birthday = Column(String(45))
    phone = Column(String(45))
    email = Column(String(45))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    country_id = Column(Integer, ForeignKey("Location.id"))
    country = relationship('Location')

    def __repr__(self): 
        return f'Customer {self.first_name}'

    @classmethod
    def find_by_id(self,session,id):
        return session.query(self).get(id)


class Location(Base):

    __tablename__ = 'Location'

    id = Column(Integer, primary_key=True)
    country_name = Column(String(45))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    @classmethod
    def find_by_id(self,session,id):
        return session.query(self).get(id) 

class Supplier(Base):

    __tablename__ = 'Supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    is_partner = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime) 
    country_id = Column(Integer, ForeignKey("Location.id"))
    country = relationship('Location')

class Product(Base):

    __tablename__ = "Product"

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    description = Column(String(45))
    price = Column(Numeric(10,2))
    color = Column(String(20))
    created_at = Column(DateTime)
    updated_at = Column(DateTime) 
    supplier_id = Column(Integer, ForeignKey("Supplier.id"))    
    supplier = relationship('Supplier')

    @classmethod
    def find_by_id(self,session,id):
        return session.query(self).get(id) 

class Order(Base):

    __tablename__ = "Order"

    id = Column(Integer, primary_key=True)
    total_products = Column(Integer)
    total_price = Column(Numeric(10,2))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status = Column(String(10))
    customer_id = Column(Integer,ForeignKey("Customer.id"))
    customer = relationship('Customer')

    @classmethod
    def find_by_status(self,session,status):
        return session.query(self).filter_by(status=status).all()

class OrderItems(Base):

    __tablename__ = "OrderItems"

    order_id = Column(Integer, ForeignKey("Order.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("Product.id"), primary_key=True)
    quantity = Column(Integer)
    item_total_price =  Column(Numeric(10,2))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    order = relationship('Order')
    product = relationship('Product')