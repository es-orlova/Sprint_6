import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        """Открывает указанный URL в браузере."""
        self.driver.get(url)

    @allure.step("Найти видимый элемент по локатору {locator}")
    def find_element_with_wait(self, locator, time=10):
        """Найти элемент с явным ожиданием."""
        try:
            element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException(f"Не удалось найти элемент по локатору {locator} за {time} секунд")

    @allure.step("Найти кликабельный элемент по локатору {locator}")
    def find_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Проскроллить до элемента {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def click_on_element(self, locator):
        element = self.find_element_to_be_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст '{keys}' в поле {locator}")
    def send_keys_to_input(self, locator, keys):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст из элемента {locator}")
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидать, что URL будет содержать '{expected_url_part}'")
    def wait_for_url(self, expected_url_part, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.url_contains(expected_url_part))
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot on failure", attachment_type=allure.attachment_type.PNG)
            raise TimeoutException(f"URL не содержит '{expected_url_part}' по истечении {time} секунд. Текущий URL: {self.driver.current_url}")