import os
import csv
import json


class InvalidPathError(Exception):
    pass

"""
Class MyFile: Represents txt files
:name: name of the file (type str)
:directory: directory where the file is stored (type str)
:num_of_lines: number of lines of text in file (type int)
"""
class MyFile:
    def __init__(self, file_path=None):
        self.set_attributes(file_path)

    def set_attributes(self, file_path):
        try:
            self._name = os.path.basename(file_path)
            self._directory = os.path.dirname(file_path)
            with open(self._name, 'r') as file_holder:
                lines = file_holder.readlines()
                self._num_of_lines = len(lines)
        except Exception:
            raise InvalidPathError("Given path is invalid.")

    def get_name(self):
        return self._name

    def get_directory(self):
        return self._directory

    def get_num_of_lines(self):
        return self._num_of_lines

    def __str__(self):
        return f'File: {self._name} has {self._num_of_lines} number of lines.'


def write_to_csv(files, csv_handler):
    writer = csv.DictWriter(csv_handler, ['name', 'directory', 'num_of_lines'])
    writer.writeheader()
    for file in files:
        name = file.get_name()
        directory = file.get_directory()
        num_of_lines = file.get_num_of_lines()
        writer.writerow({
            'name': name,
            'directory': directory,
            'num_of_lines': num_of_lines
        })


def read_from_csv(csv_handler):
    files = []
    reader = csv.DictReader(csv_handler)
    for row in reader:
        name = row['name']
        directory = row['directory']
        file = MyFile(f'{directory}/{name}')
        files.append(file)
    return files


def write_to_json(files, json_handler):
    data = []
    for file in files:
        name = file.get_name()
        directory = file.get_directory()
        num_of_lines = file.get_num_of_lines()
        file_data = {
            'name': name,
            'directory': directory,
            'num_of_lines': num_of_lines
        }
        data.append(file_data)
    json.dump(data, json_handler, indent=3)


def read_from_json(json_handler):
    files = []
    data = json.load(json_handler)
    for item in data:
        name = item['name']
        directory = item['directory']
        file = MyFile(f'{directory}/{name}')
        files.append(file)
    return files


def main():
    files = [
        MyFile('/home/oliwier/Nauka_Pythona/lab_9/cats.txt'),
        MyFile('/home/oliwier/Nauka_Pythona/lab_9/dogs.txt')
    ]
    with open('Animals.json', 'w') as json_handler:
        write_to_json(files, json_handler)
    with open('Animals.csv', 'w') as csv_handler:
        write_to_csv(files, csv_handler)
    with open('Animals.json', 'r') as json_reader:
        files = read_from_json(json_reader)
        for each_file in files:
            print(each_file)
    with open('Animals.csv', 'r') as csv_reader:
        files = read_from_csv(csv_reader)
        for each_file in files:
            print(each_file)


if __name__ == '__main__':
    main()
