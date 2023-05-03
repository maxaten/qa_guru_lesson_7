import os.path

from pypdf import PdfReader
from tests.constants import RESOURCES_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_read_pdf():
    pdf_file_path = os.path.join(RESOURCES_PATH, 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(pdf_file_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    size = os.path.getsize(pdf_file_path)
    release_doc_ver = 'Release 0.1'

    assert size == 1739253
    assert number_of_pages == 412
    assert release_doc_ver in text
