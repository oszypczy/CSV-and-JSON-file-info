from file_info import (
    MyFile,
    write_to_csv,
    read_from_csv,
    write_to_json,
    read_from_json,
    InvalidPathError
)
from io import StringIO
from pytest import raises


def test_create_file_typical():
    file = MyFile('/home/oliwier/Nauka_Pythona/lab_9/dogs.txt')
    assert file.get_name() == 'dogs.txt'
    assert file.get_directory() == '/home/oliwier/Nauka_Pythona/lab_9'
    assert file.get_num_of_lines() == 6


def test_create_file_invalid_path():
    with raises(InvalidPathError):
        MyFile('/home/oliwier/Nauka_Pythona/lab_9/peopAAAle.txt')


def test_create_file_empty_path():
    with raises(InvalidPathError):
        MyFile()


def test_write_to_csv():
    files = [MyFile('/home/oliwier/Nauka_Pythona/lab_9/people.txt')]
    csv_handler = StringIO()
    write_to_csv(files, csv_handler)
    csv_handler.seek(0)
    csv_content = csv_handler.read()
    assert csv_content == "name,directory,num_of_lines\r\npeople.txt,/home/oliwier/Nauka_Pythona/lab_9,6\r\n" # noqa 5501


def test_read_from_csv():
    data = "name,directory,num_of_lines\r\npeople.txt,/home/oliwier/Nauka_Pythona/lab_9,6\r\n" # noqa 5501
    csv_handler = StringIO(data)
    files = read_from_csv(csv_handler)
    assert files[0].get_name() == 'people.txt'
    assert files[0].get_directory() == '/home/oliwier/Nauka_Pythona/lab_9'
    assert files[0].get_num_of_lines() == 6


def test_write_to_json():
    files = [MyFile('/home/oliwier/Nauka_Pythona/lab_9/people.txt')]
    json_handler = StringIO()
    write_to_json(files, json_handler)
    json_handler.seek(0)
    json_contest = json_handler.read()
    assert json_contest == '[\n   {\n      "name": "people.txt",\n      "directory": "/home/oliwier/Nauka_Pythona/lab_9",\n      "num_of_lines": 6\n   }\n]' # noqa 5501


def test_read_from_json():
    data = '[{"name": "people.txt", "directory": "/home/oliwier/Nauka_Pythona/lab_9", "num_of_lines": 6}]' # noqa 5501
    json_handler = StringIO(data)
    files = read_from_json(json_handler)
    assert files[0].get_name() == 'people.txt'
    assert files[0].get_directory() == '/home/oliwier/Nauka_Pythona/lab_9'
    assert files[0].get_num_of_lines() == 6
