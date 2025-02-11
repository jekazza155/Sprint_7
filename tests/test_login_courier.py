import allure
import pytest
import requests
from helps import DataCourier, Courier
from endpoints import Endpoints
from urls import Urls


class TestLoginCourier:

    @allure.title('Успешная авторизация курьера с валидными данными')
    @allure.description('Проверка успешной авторизации курьера: отправка запроса, проверка ответа и удаление курьера')
    def test_courier_login_success(self, courier):
        courier_data = courier
        response = Courier().courier_login_in_the_system_and_get_id_courier(courier_data["data"])
        assert response["status_code"] == 200
        assert response.get("id")

    @allure.title('Ошибка при авторизации курьера без обязательных полей (логин/пароль)')
    @allure.description('''Проверка ошибки при авторизации курьера без заполнения обязательных полей: отправка запроса и проверка ответа''')
    @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_login_without_login,
                                           DataCourier.invalid_data_login_without_password])
    def test_courier_login_without_parameters_failed(self, courier_data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=courier_data)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.text

    @allure.title('Ошибка при авторизации курьера с несуществующими данными')
    @allure.description('Проверка ошибки при авторизации курьера с несуществующими данными: отправка запроса и проверка ответа')
    def test_courier_login_without_null_login_failed(self):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=DataCourier.null_data_login)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text
