from .exeptions import InvalidKeysError, MissingKeysError


def check_valid_request(data: dict, valid_keys: tuple, required=False):
    if required:
        invalid_keys = []
        missing_keys = []

        for key in data.keys():
            if key not in valid_keys:
                invalid_keys.append(key)
        for key in valid_keys:
            if key not in data.keys():
                missing_keys.append(key)
        if len(invalid_keys) > 0:
            raise InvalidKeysError(valid_keys=valid_keys, invalid_keys=invalid_keys)
        if len(missing_keys) > 0:
            raise MissingKeysError(
                keys_sent=[key for key in data.key()], missing_keys=missing_keys
            )

    else:
        invalid_keys = []
        for key in data.keys():
            if key not in valid_keys:
                invalid_keys.append(key)
        if len(invalid_keys) > 0:
            raise InvalidKeysError(valid_keys=valid_keys, invalid_keys=invalid_keys)
