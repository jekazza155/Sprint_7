from faker import Faker
import requests

from endpoints import Endpoints
from urls import Urls


class DataCreateCourier:
    @staticmethod
    def generating_fake_valid_data_to_create_courier():
        fake = Faker("ru_RU")
        login = fake.user_name()
        password = fake.password()
        firstname = fake.first_name()
        data = {
            "login": login,
            "firstName": firstname,
            "password": password
        }

        return data

    @staticmethod
    def generating_fake_invalid_data_to_create_courier_without_login_field():
        fake = Faker("ru_RU")
        firstname = fake.first_name()
        password = fake.password()
        data = {
            "login": "",
            "firstName": firstname,
            "password": password
        }

        return data

    @staticmethod
    def generating_fake_invalid_data_to_create_courier_without_password_field():
        fake = Faker("ru_RU")
        login = fake.user_name()
        firstname = fake.first_name()
        data = {
            "login": login,
            "password": "",
            "firstName": firstname
        }

        return data


class DataCourier:
    valid_data_login = DataCreateCourier.generating_fake_valid_data_to_create_courier()

    invalid_data_login_without_login = DataCreateCourier.generating_fake_invalid_data_to_create_courier_without_login_field()

    invalid_data_login_without_password = DataCreateCourier.generating_fake_invalid_data_to_create_courier_without_password_field()

    null_data_login = {
        "login": "test",
        "password": "test"
    }


class Courier:

    @staticmethod
    def courier_registration_in_the_system_and_get_courier_data():
        data = DataCreateCourier.generating_fake_valid_data_to_create_courier()
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}

    @staticmethod
    def courier_login_in_the_system_and_get_id_courier(data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=data)
        return {"id": str(response.json()["id"]), "response_text": response.text, "status_code": response.status_code}

    @staticmethod
    def courier_subsequent_deletion(id):
        response = requests.delete(f'{Urls.QA_SCOOTER_URL}{Endpoints.delete_courier}{id}')
        return {"response_text": response.text, "status_code": response.status_code}


class DataOrder:
    data = {
        "firstName": "Евгений",
        "lastName": "Шилов",
        "address": "г.Мытищи",
        "metroStation": 2,
        "phone": "+7 800 000 0000",
        "rentTime": 4,
        "deliveryDate": "2025-01-24",
        "comment": "Хочу быстрее кататься!",
    }
