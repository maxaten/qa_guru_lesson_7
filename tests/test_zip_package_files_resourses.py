import os.path
from zipfile import ZipFile
from constants import RESOURCES_PATH


def test_packing_files():

    # запаковка файлов
    zip_file = 'my_file.zip'
    with ZipFile(zip_file, 'w') as archive:
        for file in os.listdir(RESOURCES_PATH):
            file_path = os.path.join(RESOURCES_PATH, file)
            if os.path.isfile(file_path):
                archive.write(file_path, os.path.basename(file_path))

    # Проверка запакованных файлов
    with ZipFile(zip_file, "r") as archive:
        for file in os.listdir(RESOURCES_PATH):
            assert file in archive.namelist()
