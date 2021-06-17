from datetime import date, datetime
from random import randint, randrange, uniform
from faker import Faker
from Models import *

def update_order_status(session,status):
    new_orders = Order.find_by_status(session,'NEW')
    size_new_orders = len(new_orders)

    for order in new_orders:
        order.status = status
        order.updated_at = datetime.now()
        session.commit()



def update_customer(session,sample):

    faker = Faker()
    max_customer_count = session.query(Customer).count()
    random_customer_ids = list(set([randrange(1,max_customer_count) for _ in range(0,sample + 1)]))

    for customer_id in random_customer_ids:
        customer = Customer.find_by_id(session,customer_id)
        customer.phone = faker.phone_number()
        customer.email = faker.email()
        customer.updated_at = datetime.now()

        session.commit()

def update_product(session,sample):

    faker = Faker()
    max_product_count = session.query(Product).count()
    random_product_ids = list(set([randrange(1,max_product_count) for _ in range(0,sample + 1)]))

    for product_id in random_product_ids:
        product = Product.find_by_id(session,product_id)
        product.color = faker.safe_color_name()
        product.updated_at = datetime.now()

        session.commit()