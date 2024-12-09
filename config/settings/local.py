from .base import *  # noqa: F403
from .base import env


ALLOWED_HOSTS: list[str] = env.list(
    "DJANGO_ALLOWED_HOSTS", default=["localhost", "0.0.0.0", "127.0.0.1"]
)
