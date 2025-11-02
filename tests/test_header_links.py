import pytest
import allure
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage 
from config import Config

@allure.suite("Тесты ссылок в хедере")
class TestHeaderLinks:

    @allure.title("Проверка перехода на главную страницу по клику на лого 'Самокат'")
    def test_click_scooter_logo_goes_to_main(self, driver):
        main_page = MainPage(driver)
        
        
        main_page.open_main_page()
        main_page.click_order_btn('top')
        
        
        main_page.click_scooter_logo()
        
        
        assert main_page.get_current_url() == Config.BASE_URL, \
            "Не произошел переход на главную страницу"

    @allure.title("Проверка перехода на 'Дзен' по клику на лого 'Яндекс' в новой вкладке")
    def test_click_yandex_logo_goes_to_dzen(self, driver):
        main_page = MainPage(driver)
        
        main_page.open_main_page()
        main_page.click_yandex_logo()
        
        
        main_page.switch_to_new_window()
        
        
        main_page.wait_for_url(Config.DZEN_URL)
        
        
        assert Config.DZEN_URL in main_page.get_current_url(), \
            "Не произошел редирект на 'Дзен'"