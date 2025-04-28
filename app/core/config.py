import os

APP_DEBUG = os.getenv("APP_DEBUG", True)
APP_TITLE = os.getenv("APP_TITLE", "FastAPI Project (Dev Unit Test)")
APP_VERSION = os.getenv("APP_VERSION", "0.0.1")
APP_DESCRIPTION = os.getenv("APP_DESCRIPTION", "FastAPI Project (Dev Unit Test)")

ROUTER_PREFIX = os.getenv("ROUTER_PREFIX", "api")
