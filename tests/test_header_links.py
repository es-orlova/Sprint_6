import pytest
import allure
from page_objects.main_page import MainPage
from config import Config

@allure.suite("Тесты ссылок в хедере")
class TestHeaderLinks:

    @allure.title("Проверка перехода на главную страницу по клику на лого 'Самокат'")
    def test_click_scooter_logo_goes_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.click_order_btn_top() 
        main_page.click_scooter_logo()
        main_page.wait_for_url(Config.BASE_URL)

    @allure.title("Проверка перехода на 'Дзен' по клику на лого 'Яндекс' в новой вкладке")
    def test_click_yandex_logo_goes_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_for_url(Config.DZEN_URL)