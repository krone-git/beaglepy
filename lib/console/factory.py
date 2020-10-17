from .interface import Console


class ConsoleFactory:
    @classmethod
    def create_new(cls, *args, console=None, **kwargs):
        if not isinstance(console, Console):
            console = cls.create_new_instance()
            cls.instantiate(console, *args, **kwargs)
        return console

    @classmethod
    def create_new_instance(cls):
        return Console()

    @classmethod
    def instantiate(cls, console, *args, **kwargs):
        pass
