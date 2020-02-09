import sqlalchemy as sa
import logging
import inspect
import json
import os

from core import exceptions
ROOT = os.path.join(os.getcwd(), "..")
path = os.path.join(ROOT, "core", "configuration.json")
with open(path) as json_file:
    _GLOBAL_CACHE = json.load(json_file)

DEFAULT_CONTEXT = "enterprise"
ENVIRONMENT_ID = os.environ.get("ENVIRONMENT_ID")
ENVIRONMENT_TYPE = os.environ.get("ENVIRONMENT_TYPE")
DATABASE_KEYS = []


def get_logger(name):
    return logging.get_logger(name)


def get(key, context=DEFAULT_CONTEXT):
    _key = f"{ENVIRONMENT_TYPE}:{context}:{key}"
    return _GLOBAL_CACHE.get(key) or os.environ.get(key) or None


def get_int(key, context=DEFAULT_CONTEXT, default=0):
    v = get(key, context)
    if not v:
        return default
    try:
        return int(v)
    except TypeError:
        logger.warning(f"[{key}] returned non-integer value [{v}]")
        return 0


def put(key, value):
    global _GLOBAL_CACHE
    _GLOBAL_CACHE[key] = value


def get_database_url(database_key, **credentials):
    if database_key not in DATABASE_KEYS:
        kwargs = {
            "database_key": database_key,
            "message": "database_key not registered",
        }
        raise exceptions.ConfigurationError(**kwargs)

    database_server_key = get("database_server_key", database_key)
    database_server_url = get("database_server_url", database_server_key)

    _url = sa.make_url(database_server_url)
    _url.database = get("database_name", database_key) or database_key

    _url.user = credentials.get("user") or _url.user
    _url.password = credentials.get("password") or _url.password

    return str(_url), repr(_url)


def function_annotation(**annotation):
    def decorator(user_function):
        def wrapper(*a, **k):
            return user_function(*a, **k)
        wrapper.annotation = annotation
        wrapper.name = user_function.__name__
        return wrapper
    return decorator


logger = get_logger(__name___)
