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
        self.driver.find_element(
            by=By.XPATH, value='//*[@id="pz-gdpr-btn-accept"]'
        ).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body",
                )
            )
        ).click()
        self.driver.find_element(by=By.XPATH, value="/html/body").click()

    def run(self):
        for row in range(1, 7):
            candidate = self.get_best_candidate()
            webdriver.ActionChains(self.driver).send_keys(candidate).send_keys(
                Keys.ENTER
            ).perform()
            sleep(3)
            shadow_section = self.driver.execute_script(
                f"return document.querySelector('game-app').shadowRoot.querySelector('#board :nth-child({row})').shadowRoot"
            )
            tiles = shadow_section.find_elements(by=By.TAG_NAME, value="game-tile")
            num_correct = 0
            for index, tile in enumerate(tiles):
                letter = tile.get_attribute("letter")
                state = tile.get_attribute("evaluation")  # correct, present, absent
                if state == "correct":
                    num_correct += 1
                    self.knowledge.correct[letter].add(int(index))
                elif state == "absent":
                    self.knowledge.exclude.add(letter)
                elif state == "correct":
                    self.knowledge.almost[letter].add(int(index) - 1)

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
