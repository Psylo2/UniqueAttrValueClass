from abc import abstractmethod, ABC


class BaseTest(ABC):
    @abstractmethod
    def _add_init_attrs(self) -> None:
        ...

    @abstractmethod
    def _update_attr_value(self, attr, val) -> None:
        ...
