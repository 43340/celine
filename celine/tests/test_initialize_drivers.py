import pytest
from celine.core.driver.driver_factory import DriverFactory, DriverType
from selenium import webdriver


driver_names = [
    (DriverType.CHROME, webdriver.Chrome),
    (DriverType.FIREFOX, webdriver.Firefox)
]


@pytest.mark.parametrize('driver_type,driver_class', driver_names)
def test_init_driver(driver_type, driver_class):
    driver = DriverFactory.start_driver(driver_type)

    assert isinstance(driver, driver_class)
