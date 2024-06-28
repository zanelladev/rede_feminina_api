from abc import ABC

from flask import Blueprint


class AppRoute(ABC):
    def __init__(self, required_authorization: bool, name: str, blueprint: Blueprint):
        self.required_authorization = required_authorization
        self.name = name
        self.blueprint = blueprint
