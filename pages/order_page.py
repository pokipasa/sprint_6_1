import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as OPL


class OrderPage(BasePage):

    name_field = OPL.name_field
    surname_field = OPL.surname_field
    address_field = OPL.address_field
    metro_field = OPL.metro_field
    metro_station_list = OPL.station_list
    phone_number_field = OPL.phone_number_field
    start_date_field = OPL.start_date_field
    rent_period_field = OPL.rent_period_field
    rent_period_list = OPL.rent_period_list
    color_checkbox = OPL.color_checkbox

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнение поля "Имя"')
    def send_name(self, name):
        self.set_text_to_element(self.name_field, name)

    @allure.step('Заполнение поля "Фамилия"')
    def send_surname(self, surname):
        self.set_text_to_element(self.surname_field, surname)

    @allure.step('Заполнение поля "Адрес"')
    def send_address(self, address):
        self.set_text_to_element(self.address_field, address)

    @allure.step('Выбор станции метро')
    def send_metro_station(self):
        self.click_on_element(self.metro_field)
        self.click_on_element(self.metro_station_list)

    @allure.step('Заполнение поля "Номер телефона"')
    def send_phone_number(self, phone_number):
        self.set_text_to_element(self.phone_number_field, phone_number)

    @allure.step('Заполнение даты начала аренды')
    def send_start_date(self, start_date):
        self.set_text_to_element(self.start_date_field, start_date)
        self.confirm_by_pressing_return(self.start_date_field)

    @allure.step('Выбор срока аренды')
    def send_rent_period(self):
        self.click_on_element(self.rent_period_field)
        self.click_on_element(self.rent_period_list)

    @allure.step('Выбор цвета самоката')
    def choose_color(self):
        self.click_on_element(self.color_checkbox)

    @allure.step('Заполнение формы "Для кого самокат')
    def fill_user_data_form(self, name, surname, address, phone_number):
        self.send_name(name)
        self.send_surname(surname)
        self.send_address(address)
        self.send_metro_station()
        self.send_phone_number(phone_number)

    @allure.step('Заполнение формы "Про аренду')
    def fill_rent_data_form(self, start_date):
        self.send_start_date(start_date)
        self.send_rent_period()
        self.choose_color()
