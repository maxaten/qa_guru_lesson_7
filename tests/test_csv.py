import csv
import os

from constants import RESOURCES_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_write_and_reader_csv():
    path_to_csv = os.path.join(RESOURCES_PATH, 'eggs.csv')

    with open(path_to_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter2'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(path_to_csv) as csvfile:
        csvreader = csv.reader(csvfile)
        expected_rows = [['Anna', 'Pavel', 'Peter2'], ['Alex', 'Serj', 'Yana']]
        found_rows = []
        for row in csvreader:
            if row in expected_rows:
                found_rows.append(row)
        assert found_rows == expected_rows

