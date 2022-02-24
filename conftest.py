import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="CHOOSE LANGUAGE: es or ru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "es":
        print("\nSTART test with LANGUAGE as 'ES'...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)


    elif language == "ru":
        print("\nSTART test with LANGUAGE as 'RU'...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("--language should be ES or RU")
    yield browser
    print("\nQUIT BROWSER..")
    browser.quit()
