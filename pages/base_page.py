import allure
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск видимого элемента')
    def find_visible_element(self, locator):
        Wait(self.driver, 10).until(exp_cond.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        element = self.find_visible_element(locator)
        element.click()

    @allure.step('Берем текст выбранного элемента')
    def get_text_from_element(self, locator):
        element = self.find_visible_element(locator)
        return element.text

    @allure.step('Заполнить поле указанными данными')
    def set_text_to_element(self, locator, text):
        element = self.find_visible_element(locator)
        element.send_keys(text)

    @allure.step('Скролл до элемента')
    def go_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переход к следующей открытой вкладке')
    def switch_to_tab(self):
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        next_handle = handles[(handles.index(current_handle) + 1) % len(handles)]
        self.driver.switch_to.window(next_handle)

    @allure.step('Подтверждение ввода значения')
    def confirm_by_pressing_return(self, locator):
        element = self.find_visible_element(locator)
        element.send_keys(Keys.RETURN)

    @allure.step('Получаем URL текущей страницы')
    def get_current_page_url(self):
        return self.driver.current_url
