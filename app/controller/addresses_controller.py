from http import HTTPStatus
from flask import current_app, jsonify, request
from sqlalchemy.exc import IntegrityError
from ..models.addresses_model import AddressModel
from flask_jwt_extended import (
    jwt_required,
    decode_token,
    get_current_user,
    get_jwt_identity,
)
from datetime import timedelta
from ..utils.exeptions import UserNotFoundError
from ..utils import check_valid_request as cvr, exeptions as ex
from ..utils.valid_keys import address_keys


def create_address(data=None):
    try:
        if data is None:
            data = request.get_json()
        user = get_jwt_identity()
        data["user_id"] = user["id"]
        cvr.check_valid_request(data=data, valid_keys=address_keys, required=False)

        new_address = AddressModel(**data)
        current_app.db.session.add(new_address)
        current_app.db.session.commit()
        print(new_address)
        return jsonify(new_address), HTTPStatus.CREATED
    except ex.InvalidKeysError as err:
        return jsonify(err.msg), HTTPStatus.BAD_REQUEST
    except ex.MissingKeysError as err:
        return jsonify(err.msg), HTTPStatus.BAD_REQUEST
