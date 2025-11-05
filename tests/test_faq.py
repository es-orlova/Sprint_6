import pytest
import allure
from page_objects.main_page import MainPage
from test_data.faq_data import faq_data


@allure.suite("Тесты главной страницы: 'Вопросы о важном'")
class TestImportantQuestions:

    @allure.title("Проверка работы аккордеона в разделе 'Вопросы о важном'")
    @allure.description("Тест проверяет, что при клике на вопрос, открывается соответствующий текст ответа.")
    @pytest.mark.parametrize("question_index, expected_text", faq_data)
    def test_faq_accordion(self, driver, question_index, expected_text):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.click_faq_question(question_index)
        actual_text = main_page.get_faq_answer_text(question_index)
        assert actual_text == expected_text, f"Текст ответа для вопроса {question_index} не совпадает"