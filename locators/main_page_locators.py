from selenium.webdriver.common.by import By


class MainPageLocators:
    order_button = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text() = 'Заказать']"]  # кнопка "Заказать" в середине главной страницы
    Q_0 = [By.XPATH, ".//div[@id = 'accordion__heading-0']"]
    A_0 = [By.XPATH, ".//div[@id = 'accordion__panel-0']"]  # "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    Q_1 = [By.XPATH, ".//div[@id = 'accordion__heading-1']"]
    A_1 = [By.XPATH, ".//div[@id = 'accordion__panel-1']"]  # "Пока что у нас так: один заказ — один самокат..."
    Q_2 = [By.XPATH, ".//div[@id = 'accordion__heading-2']"]
    A_2 = [By.XPATH, ".//div[@id = 'accordion__panel-2']"]  # "Допустим, вы оформляете заказ на 8 мая..."
    Q_3 = [By.XPATH, ".//div[@id = 'accordion__heading-3']"]
    A_3 = [By.XPATH, ".//div[@id = 'accordion__panel-3']"]  # "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    Q_4 = [By.XPATH, ".//div[@id = 'accordion__heading-4']"]
    A_4 = [By.XPATH, ".//div[@id = 'accordion__panel-4']"]  # "Пока что нет! Но..."
    Q_5 = [By.XPATH, ".//div[@id = 'accordion__heading-5']"]
    A_5 = [By.XPATH, ".//div[@id = 'accordion__panel-5']"]  # "Самокат приезжает к вам с полной зарядкой..."
    Q_6 = [By.XPATH, ".//div[@id = 'accordion__heading-6']"]
    A_6 = [By.XPATH, ".//div[@id = 'accordion__panel-6']"]  # "Да, пока самокат не привезли..."
    Q_7 = [By.XPATH, ".//div[@id = 'accordion__heading-7']"]
    A_7 = [By.XPATH, ".//div[@id = 'accordion__panel-7']"]  # "Да, обязательно. Всем самокатов! И Москве, и Московской области."