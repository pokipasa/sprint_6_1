import allure
from data import Urls
from pages.main_page import MainPage
from locators.base_page_locators import BasePageLocators as BPL
from locators.order_page_locators import OrderPageLocators as OPL
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class TestClickToLogo:

    @allure.title('Проверка перехода на страницу Дзен')
    @allure.description('По клику на логотип Яндекс происходит переход на новую вкладку, где открылась главная страница Дзен')
    def test_click_to_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_element(BPL.yandex_logo)
        main_page.switch_to_tab()
        Wait(driver, 5).until(EC.url_to_be(Urls.dzen_url))
        current_url = main_page.get_current_page_url()
        assert current_url == Urls.dzen_url

    @allure.title('Проверка перехода на главную страницу')
    @allure.description('По клику на логотип Самокат происходит переход на главную страницу')
    def test_click_to_samokat_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_element(BPL.order_button_header)
        main_page.find_visible_element(OPL.user_form_header)
        main_page.click_on_element(BPL.samokat_logo)
        main_page_url = main_page.get_current_page_url()
        assert main_page_url == Urls.main_url
