from constants import WORDS
from base import Knowledge, score_word, BaseSolver


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


class SolverHelper(BaseSolver):
    def __init__(self):
        super().__init__()
        print(f"Wordle solver initialized")

    def find_best_candidates(self):
        words = list(self.words)
        scored_candidates = sorted(words, key=score_word, reverse=True)
        return scored_candidates[:5]

    def print_best_candidates(self):
        print(f"Best candidates: {self.find_best_candidates()} [{len(self.words)}]")

    def run(self):
        while True:
            self.print_best_candidates()
            user_input = input(
                "Enter command (stop, reset, correct, almost, exclude):\n"
            )
            command, args, *_ = user_input.split(" ", maxsplit=1) + [""]
            args = args.split(" ")
            if command == "stop":
                break
            elif command == "correct":
                for letter, index in pairwise(args):
                    if len(letter) != 1:
                        continue
                    self.knowledge.correct[letter].add(int(index) - 1)
            elif command == "almost":
                for letter, index in pairwise(args):
                    if len(letter) != 1:
                        continue
                    self.knowledge.almost[letter].add(int(index) - 1)
            elif command == "exclude":
                for letter in list(args[0]):
                    self.knowledge.exclude.add(letter)
            elif command == "knowledge":
                print(self.knowledge)
            elif command == "reset":
                self.knowledge = Knowledge()
            else:
                print(f'Invalid command: "{user_input}"')
            self.update_words()


if __name__ == "__main__":
    helper = SolverHelper()
    helper.run()
