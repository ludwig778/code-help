from collections import defaultdict
from os import environ


def get_config_from_env(prefix):
    config = {}

    for key, value in environ.items():
        if key.startswith(f"{prefix}_"):
            key = key.replace(f"{prefix}_", "").lower()
            config[key] = value

    return config


def get_dict_config_from_env(prefix, dataclass=None):
    config = defaultdict(dict)

    for key, value in environ.items():
        if key.startswith(f"{prefix}_"):
            _, sub_key, key = key.split("_", 2)

            if value.lower() in ["false", "true"]:
                value = eval(v.capitalize())

            config[sub_key.lower()].update({key.lower(): value})

    if dataclass:
        for key in config.keys():
            config[key] = dataclass(key=key, **config[key])

    return config
