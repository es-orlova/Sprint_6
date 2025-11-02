import pytest
import allure
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from test_data.order_data import OrderData

@allure.suite("Тесты сценария заказа самоката")
class TestOrderScooter:

    @allure.title("Проверка полного позитивного сценария заказа самоката")
    @allure.description("Тест проверяет оба входа (верхняя и нижняя кнопки 'Заказать') и два разных набора данных.")
    @pytest.mark.parametrize(
        "button_type, user_data",
        [
            ('top', OrderData.USER_1),
            ('bottom', OrderData.USER_2)
        ]
    )
    def test_order_scooter_positive_flow(self, driver, button_type, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.accept_cookies()
        
        main_page.click_order_btn(button_type)
        
        order_page.fill_first_page(user_data)
        order_page.fill_second_page(user_data)
        
        order_page.wait_for_confirmation()
        order_page.click_confirm_order_modal()
        
        assert order_page.check_success_modal_is_visible(), \
            "Модальное окно 'Заказ оформлен' не появилось"