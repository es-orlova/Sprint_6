import pytest
import allure
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from test_data.order_data import OrderData

@allure.suite("Тесты сценария заказа самоката")
class TestOrderScooter:

    @allure.title("Проверка заказа через ВЕРХНЮЮ кнопку 'Заказать' (данные: USER_1)")
    @allure.description("Проверка полного позитивного сценария заказа самоката (вход: верхняя кнопка 'Заказать')")
    def test_order_via_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        user_data = OrderData.USER_1
        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.click_order_btn_top()
        order_page.fill_first_page(user_data)
        order_page.set_when(user_data['date'])
        order_page.set_rental_period(user_data['period'])
        order_page.check_color_black()
        order_page.set_comment(user_data['comment'])
        order_page.click_final_order_button()
        order_page.wait_for_confirmation()
        order_page.click_confirm_order_modal()
        
        assert order_page.check_success_modal_is_visible(), \
            "Модальное окно 'Заказ оформлен' не появилось (Top Button Test)"

    @allure.title("Проверка заказа через НИЖНЮЮ кнопку 'Заказать' (данные: USER_2)")
    @allure.description("Проверка полного позитивного сценария заказа самоката (вход: нижняя кнопка 'Заказать')")
    def test_order_via_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        user_data = OrderData.USER_2
        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.click_order_btn_bottom()
        order_page.fill_first_page(user_data)
        order_page.set_when(user_data['date'])
        order_page.set_rental_period(user_data['period'])
        order_page.check_color_grey()
        order_page.set_comment(user_data['comment'])
        order_page.click_final_order_button()
        order_page.wait_for_confirmation()
        order_page.click_confirm_order_modal()
        
        assert order_page.check_success_modal_is_visible(), \
            "Модальное окно 'Заказ оформлен' не появилось (Bottom Button Test)"