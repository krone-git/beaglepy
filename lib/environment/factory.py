from .interface import EnvironmentSettings

__all__ = ()


class EnvironmentSettingsFactory:
    @classmethod
    def create_new(cls, *args, **kwargs):
        settings= cls.create_new_instance()
        cls.instantiate(settings, *args, **kwargs)
        return settings

    @classmethod
    def instantiate(cls, settings, *args, **kwargs):
        pass

    @classmethod
    def create_new_instance(cls):
        return EnvironmentSettings()
