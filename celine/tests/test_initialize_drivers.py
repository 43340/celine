import pytest
from celine.core.driver.driver_factory import init_driver
from selenium import webdriver


driver_names = [
    ('chrome', webdriver.Chrome),
    ('firefox', webdriver.Firefox)
]


@pytest.mark.parametrize('driver_name,driver_class', driver_names)
def test_init_driver(driver_name, driver_class):
    driver = init_driver(driver_name)

    assert isinstance(driver, driver_class)
