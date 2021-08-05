from abc import ABC, abstractmethod
from enum import Enum, auto

from selenium.webdriver.remote.webdriver import WebDriver

from celine.core.driver.drivers import ChromeDriver, FirefoxDriver


class DriverType(Enum):
    CHROME = auto()
    FIREFOX = auto()


class DriverFactory:
    """
    Factory that initializes drivers for us.
    The factory doesn't maintain any of the instances it creates.
    """

    @staticmethod
    def start_driver(driver_type: DriverType) -> WebDriver:
        """Returns new driver instance."""

        driver_types = {
            DriverType.CHROME: ChromeDriver(),
            DriverType.FIREFOX: FirefoxDriver(),
        }

        return driver_types[driver_type].create_driver()
