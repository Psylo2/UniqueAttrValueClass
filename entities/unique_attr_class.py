from abc import ABC
from typing import TypeVar, Generic
from entities.unique_value_dict import UniqueValueDict
from exception import NotUniqueValueDictError, NotUniqueValueAttrError

T = TypeVar('T')
VT = TypeVar('VT')


class UniqueAttrClass(Generic[T], ABC):
    __unique_value_dict: UniqueValueDict = UniqueValueDict()

    def __init__(self) -> None:
        ...

    def __call__(self, *args, **kwargs) -> None:
        ...

    def __mro_entries__(self, bases) -> None:
        ...

    def __getattr__(self, attr) -> None:
        ...

    def __setattr__(self, attr: str, val: VT) -> None:
        try:
            self.__unique_value_dict.__setitem__(key=attr, item=val)
            super().__setattr__(attr, val)
        except NotUniqueValueDictError:
            raise NotUniqueValueAttrError

    def __delattr__(self, attr: str) -> None:
        if attr == "__unique_value_dict":
            return None

        self.__unique_value_dict.__delitem__(key=attr)
        self.__dict__.pop(attr, None)
        del attr

    def __del__(self):
        del self.__unique_value_dict

    def __instancecheck__(self, obj) -> None:
        return self.__subclasscheck__(type(obj))

    def __subclasscheck__(self, cls) -> None:
        ...

    def __dir__(self) -> None:
        ...

    def __repr__(self):
        return "UniqueAttrClass({!r})".format(self.__dict__)
