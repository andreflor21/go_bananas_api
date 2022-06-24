from flask import Flask

from .users_view import bp_users
from .addresses_view import bp_addresses

# from .partners_view import bp_partner
# from .orders_view import bp_orders
from .index import bp_index


def init_app(app: Flask) -> None:

    app.register_blueprint(bp_index)
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_addresses)
    # app.register_blueprint(bp_orders)
