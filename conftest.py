import pytest

from helps import Courier


@pytest.fixture()
def courier():
    courier_create = Courier().courier_registration_in_the_system_and_get_courier_data()
    courier_login = Courier().courier_login_in_the_system_and_get_id_courier(courier_create["data"])
    yield courier_create
    Courier().courier_subsequent_deletion(courier_login["id"])

@pytest.fixture()
def create_and_login_courier():
    courier_create = Courier().courier_registration_in_the_system_and_get_courier_data()
    return courier_create['data']

