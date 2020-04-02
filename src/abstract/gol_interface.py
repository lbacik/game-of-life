
from abc import ABC
from abc import abstractmethod
from ..game_of_life.field import Field


class GameOfLife(ABC):

    @abstractmethod
    def field(self) -> Field:
        pass

    @abstractmethod
    def next_generation(self) -> Field:
        pass
