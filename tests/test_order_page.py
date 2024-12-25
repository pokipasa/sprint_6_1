import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators as OPL
from locators.base_page_locators import BasePageLocators as BPL
from data import OrderData


class TestOrderPage:

    @allure.title('Проверка оформления заказа')
    @allure.description(
        'Проверка успешного оформления заказа через кнопку "Заказать" в шапке сайта, '
        'и кнопку "Заказать" на главной странице'
    )
    @pytest.mark.parametrize("order_button_locator", OrderData.order_buttons)
    def test_order_placement(self, driver, order_button_locator):
        main_page = MainPage(driver)
        main_page.click_on_element(BPL.cookie_confirm_button)
        main_page.click_on_element(order_button_locator)
        order_page = OrderPage(driver)
        order_page.fill_user_data_form(OrderData.name, OrderData.surname, OrderData.address, OrderData.phone_number)
        order_page.click_on_element(OPL.next_button)
        order_page.fill_rent_data_form(OrderData.start_date)
        order_page.click_on_element(OPL.order_button)
        order_page.find_visible_element(OPL.order_confirm_header)
        order_page.click_on_element(OPL.yes_button)
        assert order_page.find_visible_element(OPL.order_created_header)