
from abc import ABC
from abc import abstractmethod
from ..game_of_life.field import Field
from ..game_of_life.point import Point


class GameOfLife(ABC):

    @abstractmethod
    def field(self) -> Field:
        pass

    @abstractmethod
    def next_generation(self) -> Field:
        pass

    @abstractmethod
    def init_field(self, x: int, y: int, start_generation: Field) -> None:
        pass
