import random

from dictionary import WORDS

COMMON_STARTING_WORDS = [
    "rance",
    "rated",
    "ronte",
    "alter",
    "salet",
    "reast",
    "crate",
    "trace",
    "slate",
]


def score_word(word):
    score = 0
    letters = list(word)
    num_letters = len(set(letters))
    for letter in list("earot"):
        if letter in word:
            score += 6
    for letter in list("lisnc"):
        if letter in word:
            score += 5

    # decrease score of plural words
    if letters[4] == "s":
        score -= 5
    return score * num_letters * num_letters


def get_homemade_best_candidate(available_words, knowledge, attempts_used):
    if attempts_used == 0:
        return random.choice(COMMON_STARTING_WORDS)

    # Trying to be smart if we know only one letter
    known_letters = set(list(knowledge.correct.keys()) + list(knowledge.almost.keys()))
    if attempts_used < 3 and len(known_letters) < 2:
        to_exclude = set.union(known_letters, knowledge.exclude)
        words_with_other_letters = sorted(
            [
                word
                for word in WORDS
                if not any([letter in word for letter in to_exclude])
            ],
            key=score_word,
            reverse=True,
        )
        return words_with_other_letters[0]

    scored_candidates = sorted(available_words, key=score_word, reverse=True)
    return scored_candidates[0]
