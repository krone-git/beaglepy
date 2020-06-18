from abc import ABCMeta, abstractmethod
import csv, json


class FileBuilder(metaclass=ABCMeta):
    def __init__(self, *args, writer=None, **kwargs):
        self._writer = writer

    @abstractmethod
    def builde(self, data):
        pass

    def execute(self, data):
        data = self.build(data)
        return self._writer.write(data)


class FileWriter(metaclass=ABCMeta):
    def __init__(self, *args, path=None, constructor=None, **kwargs):
        self._path = path
    
    @abstractmethod
    def construct(self, data):
        raise NotImplementedError

    @abstractmethod
    def output(self, data):
        raise NotImplementedError

    def write(self, data):
        constructor = self._constructor if self._constructor \
                      else self.construct
        data = constructor(data)
        if self._path:
            self.output(data)
        return data


class FileLikeWriter(FileWriter):
    def __init__(self, *args, wrapper=None, **kwargs):
        self._wrapper = wrapper

    def construct(self, data):
        #...
        pass

    def output(self, data):
        pass


class SpreadSheetWriter(FileWriter):
    def construct(self, data):
        #...
        pass


class DelimitedTextWriter(FileWriter):
    def __init__(self, *args, delimiter=",", **kwargs):
        FileWriter.__init__(self, *args, **kwargs)
        self._delimiter = delimiter

    def output(self, data):
        with open(self._path, "w", newline="") as f:
            csv.writer(f, delimiter=self._delimiter).writerows(data)


class JsonWriter(FileWriter):
    def __init__(self, *args, jsonfmt={}, **kwargs):
        self._json_format = jsonfmt

    def construct(self, data):
        pass

    def output(self, data):
        with open(self._path, "w", **self._json_format) as f:
            json.dump(data, f)
            
