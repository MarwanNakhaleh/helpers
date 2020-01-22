import unittest
import csv
from csv_helper import FileCSVHelper
import sys, os

class TestCSVHelper(unittest.TestCase):
    def setUp(self):
        print("setting up test")

    def tearDown(self):
        print("tearing down test")

    def read_csv(self, filename):
        rows = []
        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                rows.append(row)
        return rows

    def test_write_to_csv_from_list_happy(self):
        headers = ["FirstName", "LastName"]
        data = [
            ["Marwan", "Nakhaleh"],
            ["Bob", "Jones"],
            ["Willie", "Stroker"]
        ]
        filename = "testy_boi.csv"
        FileCSVHelper.write_to_csv_from_list(headers, data, filename)
        self.assertTrue(os.path.isfile(filename))
        data.insert(0, headers)
        self.assertEqual(data, self.read_csv(filename))
        os.remove(filename)
        
    def test_write_to_csv_from_list_sad(self):
        headers = ["FirstName", "LastName"]
        data = [
            ["Marwan Nakhaleh"],
            ["Bob", "Jones"],
            ["Willie", "Stroker"]
        ]
        filename = "testy_boi.csv"
        FileCSVHelper.write_to_csv_from_list(headers, data, filename)
        self.assertFalse(os.path.isfile(filename))

if __name__ == "__main__":
    unittest.main()