from selenium.webdriver.common.by import By

class MainPageLocators:
    
    ORDER_BUTTON_TOP = (By.XPATH, "//div[starts-with(@class, 'Header_')]//button[text()='Заказать']")
    
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[starts-with(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")

    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")

    @staticmethod
    def get_faq_question(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def get_faq_answer(index):
        return (By.ID, f"accordion__panel-{index}")
    