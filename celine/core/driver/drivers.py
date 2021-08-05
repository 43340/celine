from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Driver(ABC):

    @abstractmethod
    def create_driver(self, options=None) -> WebDriver:
        """Routine to create driver for factory"""


class ChromeDriver(Driver):
    """Factory to provide Chrome driver."""

    def create_driver(self, options=None) -> WebDriver:
        return webdriver.Chrome(ChromeDriverManager().install(), options=options)


class FirefoxDriver(Driver):
    """Factory to provide Chrome driver."""

    def create_driver(self, options=None) -> WebDriver:
        return webdriver.Firefox(GeckoDriverManager().install(), options=options)

