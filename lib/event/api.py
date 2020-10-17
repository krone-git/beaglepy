from ..component.interface import NamedComponent, DescribedComponent

__all__ = (
    "Event",
    )


class Event(NamedComponent, DescribedComponent):
    def __init__(self, *args, start=0, duration=1,
                    effect=(lambda state: None), **kwargs):
        super().__init__(*args, **kwargs)
        self._start = start
        self._duration = duration
        self._effect_function = effect
