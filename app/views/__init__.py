from flask import Flask

# from .customers_view import bp_customers
# from .partners_view import bp_partner
# from .orders_view import bp_orders
from .index import bp_index


def init_app(app: Flask) -> None:

    app.register_blueprint(bp_index)
    # app.register_blueprint(bp_customers)
    # app.register_blueprint(bp_partner)
    # app.register_blueprint(bp_orders)
