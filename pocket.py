from dataclasses import asdict, make_dataclass
from json import dumps


__version__ = '0.0.1'


class Pocket:

    @property
    def dict(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.dict)


def _pocket(cls, **kwargs):
    fields = [
        (p, t) for p, t in cls.__annotations__.items()
    ] if hasattr(cls, '__annotations__') else []

    return make_dataclass(
        cls.__name__,
        fields,
        bases=(Pocket,),
        **kwargs
    )


def pocket(
    _cls=None,
    *,
    init: bool=True,
    repr: bool=True,
    eq: bool=True,
    order: bool=False,
    unsafe_hash: bool=False,
    frozen: bool=False
):

    def wrap(cls):
        return _pocket(
            cls,
            init=init,
            repr=repr,
            eq=eq,
            order=order,
            unsafe_hash=unsafe_hash,
            frozen=frozen
        )

    if _cls is None:
        return wrap

    return wrap(_cls)
