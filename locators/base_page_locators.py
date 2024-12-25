from selenium.webdriver.common.by import By


class BasePageLocators:
    yandex_logo = [By.XPATH, ".//img[@alt = 'Yandex']"]
    samokat_logo = [By.XPATH, ".//img[@alt = 'Scooter']"]
    order_button_header = [By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"]
    cookie_confirm_button = [By.XPATH, ".//button[@id='rcc-confirm-button']"]
