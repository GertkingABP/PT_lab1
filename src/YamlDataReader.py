import yaml
from DataReader import DataReader


class YamlDataReader(DataReader):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.data = None

    def read(self):
        self.read_data()

    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = yaml.safe_load(file)
        except Exception as e:
            print(f"Error reading the YAML file: {e}")
