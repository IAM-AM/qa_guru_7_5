import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = "https://demoqa.com/"
    browser.config.timeout = 2.0
    browser.config.window_height = 2560
    browser.config.window_width = 1440
    browser.open()

    yield

    browser.quit()
