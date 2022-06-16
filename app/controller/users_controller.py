from http import HTTPStatus
from flask import current_app, jsonify, request
from sqlalchemy.exc import IntegrityError
from ..models.accounts_model import UserModel
from flask_jwt_extended import create_access_token
from datetime import timedelta
from ..utils.exeptions import UserNotFoundError
from ..utils import check_valid_request as cvr, exeptions as ex
from ..utils.valid_keys import user_keys


def register(data=None):
    try:
        if data is None:
            data = request.get_json()
        cvr.check_valid_request(data=data, valid_keys=user_keys, required=True)

        password_to_hash = data.pop("password")
        new_user = UserModel(**data)
        new_user.password = password_to_hash

        current_app.db.session.add(new_user)
        current_app.db.session.commit()

        return jsonify(new_user), HTTPStatus.CREATED
    except ex.InvalidKeysError as err:
        return jsonify(err.msg), HTTPStatus.BAD_REQUEST
    except ex.MissingKeysError as err:
        return jsonify(err.msg), HTTPStatus.BAD_REQUEST
    except IntegrityError as err:
        error = str(err).split("\n")
        reason = error[0].split(".")[2].split(")")[0]
        msg = error[1]
        return (
            jsonify({"error": {"reason": reason, "message": msg}}),
            HTTPStatus.CONFLICT,
        )


def get_user_by_id(_id: int) -> dict:
    user = UserModel.query.filter_by(id=_id).first()

    cur_identity = dict(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        cpf=user.cpf,
        phone=user.phone,
    )
    return cur_identity


def login(data: dict) -> UserModel:
    auth_user = UserModel.fetch_user(data["email"], data["password"])

    cur_user = dict(
        id=auth_user.id,
        emai=auth_user.email,
        first_name=auth_user.first_name,
        last_name=auth_user.last_name,
    )

    return create_access_token(identity=cur_user, expires_delta=timedelta(hours=2))


def patch(_id: int, data: dict) -> UserModel:
    cvr.check_valid_request(data=data, valid_keys=user_keys)
    user_update = UserModel.query.filter_by(id=_id).first()
    if user_update is None:
        raise UserNotFoundError(_id=_id)
    if "password" in data:
        password_to_hash = data.pop("password")
        user_update.password = password_to_hash

    for (k, v) in data.items():
        setattr(user_update, k, v)

    current_app.db.session.commit()

    return user_update, HTTPStatus.OK
