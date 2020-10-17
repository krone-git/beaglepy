from functools import wraps

__all__ = ()

def _format_attribute_name(name):
    return str(name).strip().lower().replace(" ", "_")

def get_item_at_namespace(state, namespace):
    if namespace:
        for name in namespace:
            state = state[name]
    return state

def setitemmethod(func_name):
    def wrap_method(self, other):
        set_method = getattr(type(self._state[self._name]), func_name)
        return set_method(self._state[self._name], other)
    return wrap_method


class StateAttributeSetter:
    def __init__(self, state, name):
        self._state = state
        self._name = name

    _vars = vars()
    for k in (
        "__iadd__",
        "__isub__",
        "__imul__",
        "__imatmul__",
        "__itruediv__",
        "__ifloordiv__",
        "__imod__",
        "__ipow__",
        "__ilshift__",
        "__irshift__",
        "__iand__",
        "__ixor__",
        "__ior__"
        ):
        _vars[k] = setitemmethod(k)

    del _vars, k


class AttributeHandler:
    def __init__(self, name, namespace=[]):
        self._name = name
        self._namespace = namespace

    def get(self, state):
        state = get_item_at_namespace(state, self._namespace)
        return state[self._name]

    def set(self, state, value):
        state = get_item_at_namespace(state, self._namespace)
        state[self._name] = value
        return self

    def getdefault(self, state, default=None):
        state = get_item_at_namespace(state, self._namespace)
        if selfs._name in state:
            return self.get(state)
        else:
            return default

    def setdefault(self, state, default=None):
        state = get_item_at_namespace(state, self._namespace)
        return state.setdefault(self._name, default)

    def assign(self, state):
        state = get_item_at_namespace(state, self._namespace)
        return StateAttributeSetter(state, self._name)
