import requests
import pytest
import generators
from data import Url


@pytest.fixture
def create_courier():
    """Фикстура для создания курьера с гарантированным удалением после теста."""
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}

    # Создаем курьера и получаем его ID
    response_create = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier_body)
    courier_id = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_courier_body).json().get("id")

    yield [create_courier_body, login_courier_body, login, password]

    # Удаляем курьера только если он был создан
    if courier_id:
        requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}/{courier_id}')


@pytest.fixture
def generate_courier_data():
    """Фикстура только для генерации данных курьера без создания/удаления."""
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    creation_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}

    yield [creation_courier_body, login_courier_body]  # Ничего не удаляем