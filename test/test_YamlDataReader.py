import pytest
from src.YamlDataReader import YamlDataReader
import yaml


class TestYamlDataReader:
    @pytest.fixture
    def yaml_data_reader(self, tmp_path):
        """Создание временного YAML файла и объекта для чтения данных"""
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

        reader = YamlDataReader(str(yaml_file))
        reader.read_data()
        return reader

    def test_read_data(self, yaml_data_reader):
        """Тест успешной загрузки данных"""
        assert yaml_data_reader.data is not None, \
            "Sh-ld l-ded from YAML f-e."
        assert len(yaml_data_reader.data['students']) == 3, \
            "S-ld be all st-s."
