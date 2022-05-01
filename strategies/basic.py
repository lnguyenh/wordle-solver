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


def get_basic_best_candidate(words, knowledge, attempts_used):
    scored_candidates = sorted(words, key=score_word, reverse=True)
    return scored_candidates[0]
