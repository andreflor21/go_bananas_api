from flask import Blueprint
from http import HTTPStatus

bp_index = Blueprint("", __name__, url_prefix="/")


@bp_index.get("")
def home():

    return (
        {
            "documentation": "https://github.com/andreflor21/api-go-bananas",
            "msg": "Please visit our frontend on the following url:",
            "url": "",
        },
        HTTPStatus.OK,
    )
