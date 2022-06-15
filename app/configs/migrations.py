from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    # All imports
    # from app.models.services_model import ServicesModel
    # from app.models.address_model import AddressModel
    # from app.models.customers_model import CustomersModel
    # from app.models.partners_model import PartnersModel
    # from app.models.residences_model import ResidencesModel
    # from app.models.orders_model import OrdersModel

    Migrate(app, app.db)
