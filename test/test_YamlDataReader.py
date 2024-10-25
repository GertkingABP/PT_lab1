import pytest
from src.YamlDataReader import YamlDataReader
from src.StudentStatisticsYaml import StudentStatisticsYaml
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


def test_find_student_with_min_scores(yaml_data_reader):
    """Тест поиска студента, который набрал мин 76 по 3 дисциплинам"""
    student = yaml_data_reader.find_student_with_min_scores(min_score=76)
    assert student == "John Doe", "Should find John with 76 from 3 disc-nes."


def test_no_qualifying_student(yaml_data_reader):
    """Тест, когда нет студента с мин баллами"""
    student = yaml_data_reader.find_student_with_min_scores(min_score=100)
    assert student == "No student found with min 76 from 3 disc-nes."


def test_calculate_average_score(yaml_data_reader):
    stats = StudentStatisticsYaml(yaml_data_reader.data)
    averages = stats.calculate_average_score()
    assert round(averages['John Doe'], 2) == 97.67
    assert round(averages['Jane Brown'], 2) == 92.67
    assert round(averages['Mark Spencer'], 2) == 88.0
