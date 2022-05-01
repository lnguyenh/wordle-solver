from base import Knowledge, BaseSolver


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


class SolverHelper(BaseSolver):
    def __init__(self):
        super().__init__()
        print(f"Wordle solver initialized")

    def print_best_candidate(self):
        print(f"Best candidate: {self.get_best_candidate()} [{len(self.words)}]")

    def run(self):
        while True:
            self.print_best_candidate()
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
