from abc import ABCMeta, abstractmethod


class CollectionHandler(metaclass=ABCMeta):
    def __init__(self):
        self._collection = dict()

    @property
    def collection(self):
        return self._collection

    @abstractmethod
    def add(self, value, obj):
        raise NotImplementedError

    def reset(self):
        self._collection = dict()
        return self

    def __iter__(self):
        return self

    @abstractmethod
    def  __next__(self):
        raise NotImplementedError


class SortedCollectionHandler(CollectionHandler):
    def  __init__(self):
        CollectionHandler.__init__(self)
        self._indexes, self._pointer, self._order = 0, None, ()

    def add(self, value, obj):
        if value not in self._collection:
            self._collection[value] = []
        self._collection[value].append(obj)

    def __iter__(self):
        self._order = iter(sorted(self._collection.keys()))
        self._key = next(self._order)
        self._values = iter(self._collection[self._key])
        return self

    def __next__(self):
        try:
            return next(self._values)
        except StopIteration:
            try:
                self._key = next(self._order)
                self._values = iter(self._collection[self._key])
            except StopIteration as e:
                raise e
            else:
                return next(self)


class NullCollectionHandler(CollectionHandler):
    def add(self, value, obj):
        return self

    def __next__(self):
        raise StopIteration
