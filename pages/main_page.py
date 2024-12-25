import allure
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по вопросу, получаем ответ')
    def click_to_question_get_answer(self, q_locator, a_locator):
        self.go_to_element(q_locator)
        self.click_on_element(q_locator)
        return self.get_text_from_element(a_locator)

    @allure.step('Проверка ответа на вопрос')
    def check_answer(self, result, expected):
        return result == expected
