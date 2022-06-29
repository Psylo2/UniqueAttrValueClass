from test.base_test import BaseTest
from entities.unique_attr_class import UniqueAttrClass


class ValidTest(BaseTest):
    def __init__(self):
        self.unique_attr_class = UniqueAttrClass()
        self._add_init_attrs()
        self._delete_attr()
        self._update_attrs()

    def _add_init_attrs(self) -> None:
        print("Init attrs")
        self._update_attr_value(attr="a", val=2)
        self._update_attr_value(attr="b", val=3)
        print(self.unique_attr_class)

    def _update_attrs(self) -> None:
        print("Update Attr")
        self._update_attr_value(attr="a", val=4)
        print(self.unique_attr_class)

        self._update_attr_value(attr="a", val=3)
        print(self.unique_attr_class)

    def _delete_attr(self) -> None:
        print("Delete Attr")
        self.unique_attr_class.__delattr__("a")
        print(self.unique_attr_class)

        delattr(self.unique_attr_class, "b")
        print(self.unique_attr_class)

    def _update_attr_value(self, attr, val) -> None:
        self.unique_attr_class.__setattr__(attr=attr, val=val)
