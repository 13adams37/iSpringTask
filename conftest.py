import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language. ex: en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name").lower()
    language = request.config.getoption("language").lower()
    chrome_options = Chrome_Options()
    firefox_options = Firefox_Options()
    browser = None
    if browser_name == "chrome":
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=firefox_options)

    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")
    yield browser
    browser.quit()
