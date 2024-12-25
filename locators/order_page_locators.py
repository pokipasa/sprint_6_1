from selenium.webdriver.common.by import By
from data import OrderData


class OrderPageLocators:
    user_form_header = [By.XPATH, ".//div[text()='Для кого самокат']"]  # Заголовок "Для кого самокат"
    name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]  # Поле "Имя"
    surname_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]  # Поле "Фамилия"
    address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]  # Поле "Адрес"
    metro_field = [By.XPATH, ".//input[@placeholder='* Станция метро']"]  # Поле "Станция метро"
    station_list = [By.XPATH, ".//div[@class='select-search__select']"]  # Выпадающий список станций метро
    phone_number_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]  # Поле "Телефон"
    next_button = [By.XPATH, ".//button[text()='Далее']"]  # Кнопка "Далее"
    rent_form_header = [By.XPATH, ".//div[text()='Про аренду']"]  # Заголовок "Про аренду"
    start_date_field = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]  # Поле "Когда привезти самокат"
    rent_period_field = [By.XPATH, ".//div[@class='Dropdown-placeholder']"]  # Поле "Срок аренды"
    rent_period_list = [By.XPATH, f".//div[@class='Dropdown-option'][{OrderData.rent_period}]"]  # Выбранный срока аренды
    color_checkbox = [By.XPATH, f".//input[@id='{OrderData.color}']"]  # Чекбокс выбора цвета
    order_button = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']"]  # кнопка "Заказать" на странице ввода данных об аренде
    order_confirm_header = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"]  # Заголовок "Хотите оформить заказ?"
    yes_button = [By.XPATH, ".//button[contains(text(), 'Да')]"]  # кнопка "Да" окна подтверждения заказа
    order_created_header = [By.XPATH, ".//div[text()='Заказ оформлен']"]  # Заголовок всплывающего окна с сообщением об успешном создании заказа.