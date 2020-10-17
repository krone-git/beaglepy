from ..attribute import _format_attribute_name

__all__ = ()

_format_setting_name = _format_attribute_name


class EnvironmentSettings:
    def __init__(self):
        self._settings = dict()

    def set(self, name, value):
        name = _format_setting_name(name)
        self._settings[name] = value
        return self

    def get(self, name):
        name = _format_setting_name(name)
        return self._settings[name]

    def getdefault(self, name, default=None):
        name = _format_setting_name(name)
        if name in self._settings:
            return self._settings[name]
        else:
            return default

    def setdefault(self, name, default=None):
        name = _format_setting_name(name)
        return self._settings.setdefault(name, default)

    def updatedefault(self, settings):
        return {
            k: self.setdefault(k, v) for k, v in settings.items()
            }

    __getitem__ = get
    __setitem__ = set
