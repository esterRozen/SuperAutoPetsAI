from seleniumwire import webdriver
from seleniumwire.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

email = ""
password = ""


class GameCanvas:
    def __init__(self, driver: Chrome, canvas: WebElement):
        self.driver: Chrome = driver
        self.canvas: WebElement = canvas

    def click_at(self, x, y, duration=250):
        ActionChains(self.driver, duration).move_to_element_with_offset(self.canvas, x, y).click().perform()

    def type_and_enter(self, string: str):
        self.type(string)
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def type(self, string: str):
        ActionChains(self.driver).send_keys(string).perform()


class WebDriver:
    def __init__(self):
        driver = Chrome(ChromeDriverManager().install())
        driver.get("https://teamwood.itch.io/super-auto-pets")
        buttons = driver.find_elements(By.CLASS_NAME, "button")
        found_button = False
        for button in buttons:
            if button.accessible_name == "Run game":
                button.click()
                found_button = True
        if not found_button:
            raise ConnectionError

        # enter iframe
        wait = WebDriverWait(driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="game_drop"]')))

        # find canvas
        time.sleep(1)
        canvas = driver.find_element(By.ID, 'unity-canvas')

        # wait for the privacy policy to possibly show up
        while not any(request.path == "/api/ping/datetime" for request in driver.requests):
            time.sleep(1)
        time.sleep(1)

        # now create GameCanvas for interacting with the game
        self.game = GameCanvas(driver, canvas)

        if any(["login" in request.path for request in driver.requests]):
            # you are logged in!
            pass
        else:
            # click privacy policy, should know if you needed to
            self.game.click_at(885, 525)
            time.sleep(2)
            self._login()

    def _login(self):
        # click on email box
        self.game.click_at(600, 235)
        # enter info
        self.game.type(email)
        # click on password box
        self.game.click_at(600, 335)
        # enter info
        self.game.type(password)
        # click login
        self.game.click_at(600, 435)
        time.sleep(1)
        return

    def _dismiss_announcement(self):
        for i in range(5, 695, 20):
            self.game.click_at(275, i, duration=10)


if __name__ == '__main__':
    web = WebDriver()
