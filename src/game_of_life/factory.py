
from ..abstract.gol_interface import GameOfLife as GOLInterface
from .api import GameOfLife
from .rules.conway import ConwayRules


class Factory:

    @staticmethod
    def create(width: int, height: int) -> GOLInterface:
        rules = ConwayRules()
        return GameOfLife(width, height, rules)
