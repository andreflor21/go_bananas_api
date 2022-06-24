from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    # All imports
    # from app.models.services_model import ServicesModel
    # from app.models.address_model import AddressModel
    # from app.models.customers_model import CustomersModel
    # from app.models.partners_model import PartnersModel
    from app.models.users_model import UserModel
    from app.models.addresses_model import AddressModel

    Migrate(app, app.db)
