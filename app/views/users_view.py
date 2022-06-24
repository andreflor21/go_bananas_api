from flask import Blueprint, request, jsonify
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from ..controller import users_controller
from sqlalchemy.exc import IntegrityError
from ..utils import exeptions as ex

bp_users = Blueprint("users", __name__)


@bp_users.post("/register")
def register():
    data = request.get_json()
    return users_controller.register(data)


@bp_users.post("/login")
def login():
    try:
        data = request.get_json()
        auth_token = users_controller.login(data)

        return ({"token": auth_token}, HTTPStatus.OK)
    except ex.UserNotFoundError as err:
        return (err.serialize(), HTTPStatus.NOT_FOUND)
    except ex.WrongPasswordError as err:
        return (err.__dict__, HTTPStatus.UNAUTHORIZED)


@bp_users.patch("/user/<int:id>")
@jwt_required()
def patch(id: int):
    try:
        data = request.get_json()
        user_update = users_controller.patch(_id=id, data=data)
        return (jsonify(user_update), HTTPStatus.OK)
    except ex.InvalidKeysError as err:
        return jsonify(err.msg), HTTPStatus.BAD_REQUEST
    except ex.MissingKeysError as err:
        return jsonify(err.msg), HTTPStatus.BAD_REQUEST
    except ex.UserNotFoundError as err:
        return (err.__dict__, HTTPStatus.NOT_FOUND)


@bp_users.get("/user/<int:id>")
@jwt_required()
def get(id: int):
    try:
        user = users_controller.get_user_by_id(_id=id)
        return (jsonify(user), HTTPStatus.OK)
    except ex.UserNotFoundError as err:
        return (err.__dict__, HTTPStatus.NOT_FOUND)
