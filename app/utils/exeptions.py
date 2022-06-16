class UserNotFoundError(Exception):
    def __init__(self, _id=None, email=None, msg=" was not found!") -> None:
        id_msg = f"The user with id number:{_id}{msg}"
        email_msg = f"The user with email:{email}{msg}"
        self.id = _id
        self.email = email
        self.msg = id_msg if _id else email_msg

    def serialize(self) -> dict:
        return {"message": self.msg}


class WrongPasswordError(Exception):
    def __init__(self, msg="Please inform the correct password") -> None:
        self.msg = msg


class InvalidKeysError(Exception):
    def __init__(self, valid_keys=list, invalid_keys=list) -> None:
        self.msg = {"available_keys": valid_keys, "invalid_keys": invalid_keys}
        super().__init__(self.msg)


class MissingKeysError(Exception):
    def __init__(self, keys_sent=list, missing_keys=list) -> None:
        self.msg = {"keys_sent": keys_sent, "missing_keys": missing_keys}
        super().__init__(self.msg)


class InvalidCPFError(Exception):
    def __init__(self, cpf) -> None:
        self.msg = {"error": f"CPF: {cpf} is invalid"}
        super().__init__(self.msg)


class InvalidPhoneError(Exception):
    def __init__(self, phone) -> None:
        self.msg = {"error": f"Phone: {phone} is invalid"}
        super().__init__(self.msg)
