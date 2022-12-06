from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from base import BaseSolver


class Solver(BaseSolver):
    def __init__(self):
        super().__init__()
        self.driver = None
        self.prepare_game()
        print(f"Wordle selenium solver initialized")

    def prepare_game(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.nytimes.com/games/wordle/index.html")

        # Close the bottom gdpr window
        self.driver.find_element(
            by=By.XPATH, value='//*[@id="pz-gdpr-btn-accept"]'
        ).click()

        # Close the how-to-play modal
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.CLASS_NAME,
                    "Modal-module_closeIcon__b4z74",
                )
            )
        ).click()

        # Click somewhere in the game
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.CLASS_NAME,
                    "Board-module_boardContainer__cKb-C",
                )
            )
        ).click()

    def run(self):
        for row in range(6):
            candidate = self.get_best_candidate()
            webdriver.ActionChains(self.driver).send_keys(candidate).send_keys(
                Keys.ENTER
            ).perform()
            sleep(3)
            rows = self.driver.find_elements(by=By.CLASS_NAME, value="Row-module_row__dEHfN")
            tile_row = rows[row]
            tiles = tile_row.find_elements(by=By.CLASS_NAME, value="Tile-module_tile__3ayIZ")
            num_correct = 0
            for index, tile in enumerate(tiles):
                letter = tile.text.lower()
                state = tile.get_attribute("data-state")  # correct, present, absent
                if state == "correct":
                    num_correct += 1
                    self.knowledge.correct[letter].add(int(index))
                elif state == "absent":
                    self.knowledge.exclude.add(letter)
                elif state == "present":
                    self.knowledge.almost[letter].add(int(index))

            if num_correct == 5:
                sleep(3)
                break
            else:
                self.update_words()

        self.driver.quit()
        return


if __name__ == "__main__":
    solver = Solver()
    solver.run()
