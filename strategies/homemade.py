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
    num_letters = len(set(list(word)))
    for letter in list("earot"):
        if letter in word:
            score += 5
    for letter in list("lisnc"):
        if letter in word:
            score += 4
    return score * num_letters


def get_homemade_best_candidate(available_words, knowledge, attempts_used):
    if attempts_used == 0:
        return random.choice(COMMON_STARTING_WORDS)

    # Trying to be smart if we know only one letter
    known_letters = set(list(knowledge.correct.keys()) + list(knowledge.almost.keys()))
    if attempts_used < 3 and len(known_letters) < 2:
        return sorted(
            [
                word
                for word in WORDS
                if not any(
                    [
                        letter in word
                        for letter in set.union(known_letters, knowledge.exclude)
                    ]
                )
            ],
            key=score_word,
            reverse=True,
        )[0]

    scored_candidates = sorted(available_words, key=score_word, reverse=True)
    return scored_candidates[0]
