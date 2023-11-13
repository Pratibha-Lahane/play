import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("Headless Mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def pytest_metadata(metadata):
    # To add
    metadata["Environment"] = "Test"
    metadata["Project Name"] = "OrangeHRM"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "Credence"
    # To Remove
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)


@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("admin", "admin123", "Fail"),
    ("Admin", "admin1235", "Fail"),
    ("admin", "admin1234", "Fail"),
])
def getDataforlogin(request):
    return request.param

