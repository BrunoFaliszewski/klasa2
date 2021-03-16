from abc import ABC


class Function(ABC):
    @classmethod
    def create_function(cls, **kwargs):
        raise Exception("Something went wrong.")
