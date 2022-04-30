from base import BaseSolver


class Game(BaseSolver):
    def __init__(self, solution, starter):
        super().__init__()
        self.solution = solution
        self.starter = starter
        print(f"Targeting [{self.solution}] starting from [{self.starter}]")

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
        candidate = self.starter
        print(f"attempt #{num_attempts}: {candidate}")
        while candidate != self.solution:
            self.evaluate(candidate)
            self.update_words()
            candidate = self.get_best_candidate()
            num_attempts += 1
            print(f"attempt #{num_attempts}: {candidate}")


if __name__ == "__main__":
    game = Game("larva", "crane")
    game.run()
