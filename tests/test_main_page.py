import pytest
import allure
from data import Answers
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка открывается ответ на вопрос')
    @allure.description('По клику на поле с вопросом открывается ответ на этот вопрос')
    @pytest.mark.parametrize('q_locator, a_locator, expected_result', Answers.test_parametrs)
    def test_questions_and_answers(self, driver, q_locator, a_locator, expected_result):
        main_page = MainPage(driver)
        result = main_page.click_to_question_get_answer(q_locator, a_locator)
        assert main_page.check_answer(result, expected_result)