from datetime import datetime
from faker import Faker
from SessionConfig import *
from Models import *
from GenerateRecords import *
from UpdateRecords import *

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

# create_locations(session, 10)
# create_users(session,10)
# create_suppliers(session,10)
# create_products(session,20)
# create_orders(session,5)

# update_order_status(session,'EM ANALISE')

# update_customer(session,3)
update_product(session,4)