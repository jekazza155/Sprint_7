import allure
import pytest
import requests
from helps import DataCourier
from endpoints import Endpoints
from urls import Urls


class TestCreateCourier:

    @allure.title('Успешное создание нового курьера')
    @allure.description('Проверка успешного создания курьера: отправка запроса, проверка ответа и удаление курьера')
    def test_registration_courier_success(self, courier):
        courier_data = courier
        assert courier_data["status_code"] == 201
        assert courier_data["response_text"] == '{"ok":true}'

    @allure.title('Ошибка при попытке создания дубликата курьера')
    @allure.description('Проверка ошибки при создании курьера с уже существующими данными: отправка запроса и проверка ответа')
    def test_registration_double_courier_failed(self, courier):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier["data"])
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.text

    @allure.title('Ошибка при создании курьера без обязательных полей (логин/пароль)')
    @allure.description('Проверка ошибки при создании курьера без заполнения обязательных полей: отправка запроса и проверка ответа')
    @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_login_without_login,
                                           DataCourier.invalid_data_login_without_password])
    def test_courier_registration_without_parameters_failed(self, courier_data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text
