import allure
from page_objects.base_page import BasePage
from locators.order_page_locators import OrderPageLocators




class OrderPage(BasePage):

    @allure.step("Заполнить поле Имя")
    def set_fild_name(self, name):
        self.send_keys_to_input(OrderPageLocators.NAME, name)

    @allure.step("Заполнить поле Фамилия")
    def set_fild_surname(self, surname):
        self.send_keys_to_input(OrderPageLocators.SURNAME, surname)

    @allure.step("Заполнить поле Адрес")
    def set_fild_adress(self, adress):
        self.send_keys_to_input(OrderPageLocators.ADDRESS, adress)

    @allure.step("Заполнить поле Станция метро")
    def set_fild_metro(self, metro_station_name):
        self.send_keys_to_input(OrderPageLocators.METRO_INPUT, metro_station_name)
        metro_option_locator = OrderPageLocators.metro_locator(metro_station_name)
        self.click_on_element(metro_option_locator)

    @allure.step("Заполнить поле Телефон")
    def set_fild_phone_number(self, phone_number):
        self.send_keys_to_input(OrderPageLocators.PHONE_NUMBER, phone_number)
    
    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить первую страницу формы заказа")
    def fill_first_page(self, user_data):
        self.set_fild_name(user_data['name'])
        self.set_fild_surname(user_data['surname'])
        self.set_fild_adress(user_data['address'])
        self.set_fild_metro(user_data['metro'])
        self.set_fild_phone_number(user_data['phone'])
        self.click_next_button()

    @allure.step("Заполнить поле 'Когда привезти'")
    def set_when(self, date):
        self.send_keys_to_input(OrderPageLocators.WHEN_INPUT, date)
        self.click_on_element(OrderPageLocators.TODAY_DATE_IN_CALENDAR)

    @allure.step("Выбрать срок аренды")
    def set_rental_period(self, period_text):
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        period_locator = OrderPageLocators.get_rental_period_option(period_text)
        self.scroll_to_element(period_locator)
        self.click_on_element(period_locator)

    @allure.step("Выбрать черный цвет самоката")
    def check_color_black(self):
        self.click_on_element(OrderPageLocators.COLOR_CHECKBOX_BLACK)

    @allure.step("Выбрать серый цвет самоката")
    def check_color_grey(self):
        self.click_on_element(OrderPageLocators.COLOR_CHECKBOX_GREY)

    @allure.step("Заполнить поле 'Комментарий'")
    def set_comment(self, comment):
        self.send_keys_to_input(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Нажать финальную кнопку 'Заказать'")
    def click_final_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_FINAL)

    @allure.step("Заполнить вторую страницу формы заказа")
    def fill_second_page(self, user_data):
        self.set_when(user_data['date'])
        self.set_rental_period(user_data['period'])
        self.check_color(user_data['color'])
        self.set_comment(user_data['comment'])
        self.click_final_order_button()
    
    @allure.step("Ожидать появления модального окна подтверждения")
    def wait_for_confirmation(self):
        self.find_element_with_wait(OrderPageLocators.CONFIRM_MODAL)

    @allure.step("Нажать 'Да' в модальном окне подтверждения")
    def click_confirm_order_modal(self):
        self.click_on_element(OrderPageLocators.CONFIRM_MODAL_YES_BUTTON)
    
    @allure.step("Проверить, что модальное окно 'Заказ оформлен' появилось")
    def check_success_modal_is_visible(self):
        try:
            self.find_element_with_wait(OrderPageLocators.SUCCESS_MODAL, 5)
            return True
        except:
            return False