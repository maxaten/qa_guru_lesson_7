import os.path
import requests

from tests.constants import PROJECT_PATH_TMP


def test_downloaded_file_size():
    # TODO сохранять и читать из tmp, использовать универсальный путь
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    r = requests.get(url)
    download_file_path = os.path.join(PROJECT_PATH_TMP, 'selenium_logo.png')
    with open(download_file_path, 'wb') as file:
        file.write(r.content)

    size = os.path.getsize(download_file_path)
    assert size == 30803

