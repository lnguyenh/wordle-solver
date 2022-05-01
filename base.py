from collections import defaultdict

from dictionary import WORDS
from strategies import WordleStrategies


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
        self.attempts_used = 0
        self.reset()

    def reset(self):
        self.knowledge = Knowledge()
        self.words = set(WORDS)

    def update_words(self):
        words = list(self.words)
        for word in words:
            for letter in self.knowledge.exclude:
                if (
                    letter in word
                    and letter not in self.knowledge.correct
                    and letter not in self.knowledge.almost
                ):
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
        candidate = WordleStrategies.HOMEMADE(words, self.knowledge, self.attempts_used)
        self.attempts_used += 1
        return candidate
