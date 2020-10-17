from itertools import chain

class _A:
    names = ("_A",)

    def __new__(cls):
        cls.names = tuple(chain(
            *(base.names for base in cls.__bases__),
            cls.names
            ))
        return super().__new__(cls)


class A(_A):
    names = ("A",)

    def __init__(self):
        self.dict = dict()

    def __new__(cls):
        cls.__getitem__ = cls.get
        cls.__setitem__ = cls.set
        return super().__new__(cls)

    def set(self, key, value):
        self.dict[key] = value
        return self

    def get(self, key):
        return self.dict[key]


class B:
    names = ("B",)

    def __new__(cls):
        def getattribute(func):
            def _getattribute(self, name):
                _dict = object.__getattribute__(self, "dict")
                if name.isupper() and name.lower() in _dict:
                    return name.lower()
                else:
                    return func(self, name)
            return _getattribute

        def setattribute(func):
            def _setattribute(self, name, value):
                try:
                    _dict = object.__getattribute__(self, "dict")
                except AttributeError as e:
                    _dict = dict()
                if name.isupper() and name.lower() in _dict:
                    raise ValueError("cannot set attribute.")
                else:
                    return func(self, name, value)
            return _setattribute

        cls.__getattribute__ = getattribute(cls.__getattribute__)
        cls.__setattr__ = setattribute(cls.__setattr__)
        return super().__new__(cls)


class C:

    names = ("C",)
    def __new__(cls):
        def getattribute(func):
            def _getattribute(self, name):
                _dict = object.__getattribute__(self, "dict")
                if name.islower() and name in _dict:
                    return _dict[name]
                else:
                    return func(self, name)
            return _getattribute

        def setattribute(func):
            def _setattribute(self, name, value):
                try:
                    _dict = object.__getattribute__(self, "dict")
                except AttributeError as e:
                    _dict = dict()
                if name.islower() and name in _dict:
                    raise ValueError("cannot set attribute.")
                else:
                    return func(self, name, value)
            return _setattribute

        cls.__getattribute__ = getattribute(cls.__getattribute__)
        cls.__setattr__ = setattribute(cls.__setattr__)
        return super().__new__(cls)

class D:
    names = ("D",)
    def __new__(cls):
        def format_keyvalue(func):
            def _format_keyvalue(self, key, value):
                return func(self, str(key).lower(), str(value).upper())
            return _format_keyvalue

        cls.set = format_keyvalue(cls.set)
        return super().__new__(cls)


class E:
    names = ("E",)


class X(A, B, C, D, E):
    names = ("X",)

class X2(A, B, C, D, E):
    def set(self, name, value):
        print("setting", name, "to", value)
        return super().set(name, value)

    def get(self, name):
        print("getting", name)
        return super().get(name)


x = X()
x.set("a", 0)
x["b"] = 1
print("x", x.get("a"))
print("x", x["a"])
print()
x2 = X2()
x2.set("c", 2)
x2["d"] = 3
print("x2", x2.get("c"))
print("x2", x2["d"])
