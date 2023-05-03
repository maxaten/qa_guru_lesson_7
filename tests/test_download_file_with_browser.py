import os
import time
import zipfile
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from constants import PROJECT_PATH_TMP

# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_download_file():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": PROJECT_PATH_TMP,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)


    size_file = os.path.getsize(os.path.join(PROJECT_PATH_TMP, 'pytest-main.zip'))
    assert size_file == 1565002

    with zipfile.ZipFile(os.path.join(PROJECT_PATH_TMP, 'pytest-main.zip'), 'r') as zip_file:
        expected_files = ['pytest-main/', 'pytest-main/.github/']
    assert all(file in zip_file.namelist() for file in expected_files)

