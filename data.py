import datetime
from datetime import date
from locators.base_page_locators import BasePageLocators as BPL
from locators.main_page_locators import MainPageLocators as MPL


class Urls:
    main_url = 'https://qa-scooter.praktikum-services.ru/'
    dzen_url = 'https://dzen.ru/?yredirect=true'


class Answers:
    test_parametrs = [
        (MPL.Q_0, MPL.A_0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (MPL.Q_1, MPL.A_1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                           'можете просто сделать несколько заказов — один за другим.'),
        (MPL.Q_2, MPL.A_2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                           'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                           'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (MPL.Q_3, MPL.A_3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (MPL.Q_4, MPL.A_4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (MPL.Q_5, MPL.A_5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (MPL.Q_6, MPL.A_6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (MPL.Q_7, MPL.A_7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'),
    ]


class OrderData:
    name = 'Гриша'
    surname = 'Кабачков'
    address = 'Щербакова ул. 24 корп. 1'
    phone_number = '+79119625999'
    start_date = (date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
    rent_period = 2
    color = 'black'
    order_buttons = [BPL.order_button_header, MPL.order_button]