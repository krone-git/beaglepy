from abc import ABCMeta, abstractmethod


class ConsoleFactory:
    def create(cls, *args, **kwargs):
        return StdoutConsole(*args, **kwargs)


class Console(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        pass
    
    def print(self, *args, **kwargs):
        raise NotImplementedError


class StdoutConsole(Console):
    def print(self, message, *args **kwargs):
        print(message)
