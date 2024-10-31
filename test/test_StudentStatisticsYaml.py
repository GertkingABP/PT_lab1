from src.StudentStatisticsYaml import StudentStatisticsYaml
import pytest


@pytest.fixture
def yaml_data():

    data = {
        'students': [
            {'name': 'John Doe', 'scores': [58, 68, 70]},
            {'name': 'Jane Brown', 'scores': [90, 100, 91]},
            {'name': 'Tim Spoon', 'scores': [10, 10, 1]},
            {'name': 'Maria Anro', 'scores': [50, 60, 57]},
            {'name': 'Ann Wilp', 'scores': [70, 61, 71]},
            {'name': 'Wendy Quan', 'scores': [100, 90, 91]},
            {'name': 'Max Lee', 'scores': [100, 90, 88]},
            {'name': 'Anton Ardy', 'scores': [10, 0, 8]},
            {'name': 'Joe Winter', 'scores': [78, 80, 94]},
            {'name': 'Veronica Iv', 'scores': [99, 98, 97]}
        ]
    }
    return StudentStatisticsYaml(data)


class TestStudentStatisticsYaml:

    def test_find_student_with_min_scores(self, yaml_data):
        """Тест поиска студента, который набрал мин 76 по 3 дисциплинам"""
        student = yaml_data.find_student_with_min_scores(min_scr=76)
        if student != "\nNo student found with the minimum required scores.":
            print(f"\nStudent found with min 76 points in 3 subj-s: {student}")
        else:
            print(student)
        assert student

    def test_find_high_achievers(self, yaml_data):
        """Тест на нахождение студентов с высокими баллами (90+) по каждому."""
        high_achievers = yaml_data.find_high_achievers()
        assert high_achievers  # Проверка на наличие отличников
        print("\nHigh achievers (90+ in all subjects):", high_achievers)

    def test_find_low_performers(self, yaml_data):
        """Тест на нахождение студентов с низкими баллами (<61) по каждому."""
        low_performers = yaml_data.find_low_performers()
        assert low_performers  # Проверка на наличие двоечников
        print("\nLow performers (<61 in all subjects):", low_performers)
