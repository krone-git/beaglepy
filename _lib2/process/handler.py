form abc import ABCMeta, abstractmethod


class ProcessHandler(ProcessHandlerType):
    def execute(self, history_handler, state_handler, process_handler):
        pass


class IterationProcessHandler(ProcessHandlerType):
    def __init__(self, iterator=None):
        self._iterator = iterator

    def execute(self, history_handler, state_handler, console_handler):
        while self._iterator.is_active():
            state_handler.new()
            self._iterator.feed(state_handler)
            for process in self._processes:
                process.execute(state_handler, console_handler)
            history_handler.add(state_handler.get())
            self._iterator.next(state_handler)


class ProcessHandlerType(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, history_handler, state_handler, process_handler):
        raise NotImplementedError
