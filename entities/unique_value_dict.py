from abc import ABC
from typing import TypeVar, MutableMapping, Generic, Dict, Set, Iterator
from exception import NotUniqueValueDictError

KT = TypeVar('KT')
VT = TypeVar('VT')


class UniqueValueDict(MutableMapping[KT, VT], Generic[KT, VT], ABC):

    def __init__(self) -> None:
        self.exists_values_set: Set[VT] = set()
        self._dict: MutableMapping[str, VT] = {}

    def __setitem__(self, key: KT, item: VT) -> None:
        exists_value = self._dict.get(key, {})
        if exists_value:
            self.__update_exists_item(key=key, item=item, exists_value=exists_value)
            return None

        self.__insert_unique_value(key=key, item=item)

    def __delitem__(self, key: KT) -> None:
        exists_value = self._dict.get(key, {})

        if exists_value:
            self.exists_values_set.discard(key)
            self._dict.__delitem__(key)

            self.__dict__['exists_values_set'] = self.exists_values_set
            self.__dict__['_dict'] = self._dict

    def __delattr__(self, item):
        if item == "exists_values_set" or "_dict":
            return None

        del item

    def __repr__(self):
        return f'{self._dict}'

    def __len__(self) -> int:
        ...

    def __getitem__(self, k: KT) -> VT:
        ...

    def __iter__(self) -> Iterator[KT]:
        ...

    def __update_value(self, __m: Dict[KT, VT]) -> None:
        for key, value in __m.items():
            self.__setitem__(key, value)

    def _check_unique_value(self, value: VT) -> None:
        if value in self.exists_values_set:
            raise NotUniqueValueDictError

    def __insert_unique_value(self, key: KT, item: VT) -> None:
        self._check_unique_value(value=item)
        self.exists_values_set.add(item)
        self._dict[key] = item

    def __update_exists_item(self, key: KT, item: VT, exists_value: Dict[KT, VT]) -> None:
        self._check_unique_value(value=item)

        self.exists_values_set.discard(exists_value)
        self.exists_values_set.add(item)
        self._dict[key] = item
