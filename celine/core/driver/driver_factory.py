from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory(ABC):
    """
    Factory that initializes drivers for us.
    The factory doesn't maintain any of the instances it creates.
    """

    def init_driver(self, driver_type) -> WebDriver:
        """Returns new driver instance."""


class ChromeDriverFactory(DriverFactory):
    """Factory to provide Chrome driver."""

    def init_driver(self, options=None) -> WebDriver:
        return webdriver.Chrome(ChromeDriverManager().install(), options=options)


class FirefoxDriverFactory(DriverFactory):
    """Factory to provide Chrome driver."""

    def init_driver(self, options=None) -> WebDriver:
        return webdriver.Firefox(GeckoDriverManager().install(), options=options)


def init_driver(driver_name):
    driver_types = {
        'chrome': ChromeDriverFactory(),
        'firefox': FirefoxDriverFactory(),
    }

    return driver_types[driver_name].init_driver()
