from enum import Enum

from strategies.basic import get_basic_best_candidate
from strategies.homemade import get_homemade_best_candidate
from strategies.scrabble import get_scrabble_best_candidate


class WordleStrategies(Enum):
    BASIC = get_basic_best_candidate
    SCRABBLE = get_scrabble_best_candidate
    HOMEMADE = get_homemade_best_candidate
