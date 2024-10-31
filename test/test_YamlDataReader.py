import pytest
from src.YamlDataReader import YamlDataReader
import yaml


@pytest.fixture
def yaml_test_data(tmp_path):
    """Фикстура создания врем-го YAML-файла с тестовыми данными"""
    test_data = {
        'students': [
            {'name': 'John Doe', 'scores': [100, 96, 97]},
            {'name': 'Jane Brown', 'scores': [99, 89, 90]},
            {'name': 'Mark Spencer', 'scores': [89, 88, 87]}
        ]
    }

    yaml_file = tmp_path / "testfile.yaml"
    with yaml_file.open('w') as f:
        yaml.dump(test_data, f)

    return yaml_file


@pytest.fixture
def yaml_data_reader(yaml_test_data):
    """Фикстура создания объекта и чтения данных из врем-го файла"""
    reader = YamlDataReader(str(yaml_test_data))
    reader.read_data()
    return reader


def test_read_data(yaml_data_reader):
    """Тест успешной загрузки данных"""
    assert yaml_data_reader.data is not None, "Data loaded from YAML file."
    assert len(yaml_data_reader.data['students']) == 3, "Should be all stud-s."
