from selenium.webdriver.common.by import By

class OrderPageLocators:

    
    NAME = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")
    SURNAME = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")
    ADDRESS = (By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]")
    METRO_INPUT = (By.XPATH, "//input[contains(@placeholder, '* Станция метро')]")
    PHONE_NUMBER = (By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    
    @staticmethod
    def metro_locator(metro):
        return (By.XPATH, f"//div[text()='{metro}']")

    
    WHEN_INPUT = (By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]")
    
    TODAY_DATE_IN_CALENDAR = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
    
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    
    
    @staticmethod
    def get_rental_period_option(period_text):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period_text}']")

    COLOR_CHECKBOX_BLACK = (By.ID, "black")
    COLOR_CHECKBOX_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]")
    
    ORDER_BUTTON_FINAL = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    
    CONFIRM_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    CONFIRM_MODAL_YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    
    SUCCESS_MODAL = (By.XPATH, "//div[text()='Заказ оформлен']")