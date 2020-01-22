import csv

class FileCSVHelper:
    @staticmethod
    def write_to_csv_from_list(headers: list, data: list, filename: str):
        for row in data:
            if len(row) != len(headers):
                print("unequal data")
                return False
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in data:
                row_dict = {}
                for x in range(0, len(row)):
                    row_dict[headers[x]] = row[x]
                writer.writerow(row_dict)
