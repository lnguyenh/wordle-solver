from base import BaseSolver


class Game(BaseSolver):
    def __init__(self, solution):
        super().__init__()
        self.solution = solution
        print(f"Targeting [{self.solution}]")

    def evaluate(self, candidate):
        for i, letter in enumerate(candidate):
            if letter == self.solution[i]:
                self.knowledge.correct[letter].add(i)
            elif letter in self.solution:
                self.knowledge.almost[letter].add(i)
            else:
                self.knowledge.exclude.add(letter)
        return

    def run(self):
        num_attempts = 1
        candidate = self.get_best_candidate()
        print(f"attempt #{num_attempts}: {candidate}")
        while candidate != self.solution:
            self.evaluate(candidate)
            self.update_words()
            candidate = self.get_best_candidate()
            num_attempts += 1
            print(f"attempt #{num_attempts}: {candidate}")


if __name__ == "__main__":
    game = Game("zesty")
    game.run()
