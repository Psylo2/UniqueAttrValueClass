from test.base_test import BaseTest
from entities.unique_attr_class import UniqueAttrClass


class InvalidInitTest(BaseTest):
    def __init__(self):
        self.unique_attr_class = UniqueAttrClass()
        self._add_init_attrs()

    def _add_init_attrs(self) -> None:
        print("Invalid Init attrs")
        self._update_attr_value(attr="a", val=2)
        self._update_attr_value(attr="b", val=2)
        print(self.unique_attr_class)

    def _update_attr_value(self, attr, val) -> None:
        self.unique_attr_class.__setattr__(attr=attr, val=val)
