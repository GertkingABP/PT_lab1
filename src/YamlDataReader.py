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

    def find_student_with_min_scores(self, min_score=76):
        """Поиск студентов, набравших минимум 76 по 3 дисциплинам"""
        if self.data is None:
            print("Data is not loaded. Please read the file first.")
            return None

        qualifying_students = []
        for student in self.data.get('students', []):
            scores = student.get('scores', [])
            high_scores = [score for score in scores if score >= min_score]
            if len(high_scores) >= 3:
                qualifying_students.append(student['name'])

        if qualifying_students:
            print(f"""Student with at least
            {min_score} p-ts in 3 sub-s: {qualifying_students[0]}""")
            return qualifying_students[0]  # первый студент
        else:
            print("No student found with minimum 76 points in 3 subjects.")
            return "No student found with min 76 from 3 disc-nes."
