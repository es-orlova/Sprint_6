import allure
from page_objects.base_page import BasePage
from locators.main_locators import MainPageLocators
from config import Config

class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.driver.get(self.url)

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_on_element(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            allure.attach("Кнопка 'Куки' не найдена или уже принята", name="Cookie Info", attachment_type=allure.attachment_type.TEXT)
            print("Кнопка 'Куки' не найдена или уже принята")

    @allure.step("Проскроллить до секции 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Проскроллить и кликнуть на вопрос в FAQ по индексу: {index}")
    def click_faq_question(self, index):
        question_locator = MainPageLocators.get_faq_question(index)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Получить текст ответа в FAQ по индексу: {index}")
    def get_faq_answer_text(self, index):
        answer_locator = MainPageLocators.get_faq_answer(index)
        return self.get_text_from_element(answer_locator)

    @allure.step("Нажать на лого 'Самокат'")
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на лого 'Яндекс'")
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Нажать на кнопку 'Заказать'")
    def click_order_btn(self, button_type):
        if button_type == 'top':
            locator = MainPageLocators.ORDER_BUTTON_TOP
        elif button_type == 'bottom':
            locator = MainPageLocators.ORDER_BUTTON_BOTTOM
            self.scroll_to_element(locator) 
        else:
            raise ValueError("Неверный тип кнопки: 'top' или 'bottom'")
        
        self.click_on_element(locator)