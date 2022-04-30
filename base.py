from collections import defaultdict

from constants import WORDS

SCRABBLE_SCORE = {
    "a": 1,
    "c": 3,
    "b": 3,
    "e": 1,
    "d": 2,
    "g": 2,
    "f": 4,
    "i": 1,
    "h": 4,
    "k": 5,
    "j": 8,
    "m": 3,
    "l": 1,
    "o": 1,
    "n": 1,
    "q": 10,
    "p": 3,
    "s": 1,
    "r": 1,
    "u": 1,
    "t": 1,
    "w": 4,
    "v": 4,
    "y": 4,
    "x": 8,
    "z": 10,
}


def scrabble_score(word):
    return -sum([SCRABBLE_SCORE[letter] for letter in list(word)])


def base_score(word):
    score = 0
    num_letters = len(set(list(word)))
    for letter in list("earot"):
        if letter in word:
            score += 5
    for letter in list("lisnc"):
        if letter in word:
            score += 4
    return score * num_letters


def score_word(word):
    return base_score(word)
    # return scrabble_score(word)


class Knowledge:
    def __init__(self):
        self.correct = defaultdict(set)
        self.almost = defaultdict(set)
        self.exclude = set()

    def update(self, new_knowledge):
        return

    def __str__(self):
        return f"[correct: {dict(self.correct)}] [almost: {dict(self.almost)}] [exclude: {self.exclude}]"


class BaseSolver:
    def __init__(self):
        self.knowledge = None
        self.words = None
        self.reset()

    def reset(self):
        self.knowledge = Knowledge()
        self.words = set(WORDS)

    def update_words(self):
        words = list(self.words)
        for word in words:
            for letter in self.knowledge.exclude:
                if letter in word:
                    self.words.discard(word)
                    break
            for letter, positions in self.knowledge.correct.items():
                for position in positions:
                    if word[position] != letter:
                        self.words.discard(word)
            for letter, positions in self.knowledge.almost.items():
                if letter not in word:
                    self.words.discard(word)
                for position in positions:
                    if word[position] == letter:
                        self.words.discard(word)

    def get_best_candidate(self):
        words = list(self.words)
        scored_candidates = sorted(words, key=score_word, reverse=True)
        return scored_candidates[0]
