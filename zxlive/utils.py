import os

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path: str) -> str:
    return os.path.join(_ROOT, path)
