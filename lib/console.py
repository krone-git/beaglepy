from abc import ABCMeta, abstractmethod


class Console(metaclass=ABCMeta):
    def print(self, *args, **kwargs):
        raise NotImplementedError


class StdoutConsole(Console):
    def print(self, message, *args **kwargs):
        print(message)
