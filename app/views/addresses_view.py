from flask import Blueprint, request, jsonify
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from ..controller import addresses_controller
from sqlalchemy.exc import IntegrityError
from ..utils import exeptions as ex


bp_addresses = Blueprint("addresses", __name__)


@bp_addresses.post("/user/<int:id>/address")
@jwt_required()
def create(id: int):
    data = request.get_json()
    return addresses_controller.create_address(data)
