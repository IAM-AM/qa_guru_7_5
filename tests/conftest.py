import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def set_browser_windows_size():
    browser.config.window_height = 2560
    browser.config.window_width = 1440
    yield
    browser.quit()
