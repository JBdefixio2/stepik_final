Данный проект реализован в рамках прохождения курса "Автоматизация тестирования с помощью Selenium и Python" на stepik.org.

Структура проекта:

pages:
base_page.py - базовый класс страниц
basket_page.py - страница корзины
locators.py - локаторы для страниц
login_page.py - страница входа и регистрации
main_page.py - главная страница сайта
product_page.py - страница продукта
_init_.py - файл инициализации
conftest.py - инициализация браузера и его закрытие
pytest.ini - описание маркеров
readme.md - файл, который Вы сейчас читаете
requirements.txt - файл с пакетами, необходимыми для работы с данным проектом
test_main_page.py - тестовый файл (для тестирования main_page)
test_product_page.py - тестовый файл (для тестирования product_page)
ВАЖНО!!! Перед запуском тестов на компьютере убедитесь, что:

Путь к chromedriver прописан в PATH
Вы установили необходимые пакеты при помощи команды: pip install -r requirements.txt