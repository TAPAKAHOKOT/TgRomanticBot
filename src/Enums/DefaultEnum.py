from enum import Enum


class DefaultEnum(Enum):
    def __repr__(self):
        return str(self.value)