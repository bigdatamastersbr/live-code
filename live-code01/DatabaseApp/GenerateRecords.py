from datetime import date, datetime
from random import randint, randrange, uniform
from faker import Faker
from Models import *

def create_locations(session,sample):
    faker = Faker()
    locations = []

    for _ in range(0,sample + 1):
        l = Location(country_name=faker.country(), created_at=faker.past_datetime(),updated_at=datetime.now())
        locations.append(l)

    session.add_all(locations)
    session.commit()



def create_users(session,sample):
    faker = Faker()
    users = []

    max_location_records = session.query(Location).count()

    for _ in range(0,sample + 1):
        location = session.query(Location).get(randrange(1,max_location_records))
        user = Customer(first_name=faker.first_name(), 
                        last_name=faker.last_name(), 
                        birthday=faker.date_of_birth(),
                        phone=faker.phone_number(),
                        email=faker.email(),
                        created_at=faker.past_datetime(),
                        updated_at=datetime.now(),
                        country=location)
        users.append(user)
    
    session.add_all(users)
    session.commit()

def create_suppliers(session,sample):
    faker = Faker()
    suppliers = []

    max_location_records = session.query(Location).count()

    for _ in range(0,sample + 1):
        location = session.query(Location).get(randrange(1,max_location_records))
        supplier = Supplier(name=faker.company(),
                            is_partner=True, 
                            created_at=faker.past_datetime(),
                            updated_at=datetime.now(),
                            country=location)

        suppliers.append(supplier)
    
    session.add_all(suppliers)
    session.commit()

def create_products(session,sample):
    faker = Faker()
    products = []

    max_supplier_records = session.query(Supplier).count()

    for _ in range(0,sample + 1):
        supplier = session.query(Supplier).get(randrange(1,max_supplier_records))
        product = Product(name=''.join(faker.random_letters()),
                          description=faker.random_element(),
                          price=round(uniform(10,5000),2),
                          color=faker.safe_color_name(),
                          supplier=supplier,
                          created_at=faker.past_datetime(),
                          updated_at=datetime.now())
        products.append(product)
    
    session.add_all(products)
    session.commit()

def create_orders(session,sample):
    faker = Faker()

    max_customer_records = session.query(Customer).count()
    max_product_records = session.query(Product).count()

    for _ in range(0,sample + 1):
        customer = session.query(Customer).get(randrange(1,max_customer_records))
        items_qtde = randrange(1,10) # Qtde de Itens no Carrinho para uma Ordem
        choosed_product_ids = [randrange(1,max_product_records) for _ in range(1, items_qtde)]
        total_price = sum([Product.find_by_id(session,id).price for id in choosed_product_ids])

        order = Order(
            total_products=len(choosed_product_ids),
            total_price=total_price,
            created_at=faker.past_datetime(),
            updated_at=datetime.now(),
            status='NEW',
            customer=customer
        )

        session.add(order)
        session.flush()

        order_items = []
        for product_id in list(set(choosed_product_ids)):
            qtde = choosed_product_ids.count(product_id)
            product = Product.find_by_id(session,product_id)
            order_item = OrderItems(
                order=order,
                product=product,
                quantity=qtde,
                item_total_price=product.price * qtde,
                created_at=faker.past_datetime(),
                updated_at=datetime.now(),
            )

            order_items.append(order_item)
        session.add_all(order_items)
    
    session.commit()


        