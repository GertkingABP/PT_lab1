class StudentStatisticsYaml:
    def __init__(self, data):
        self.data = data.get('students', [])

    def calculate_average_score(self):
        """Вычисление среднего балла каждого студента."""
        averages = {}
        for std in self.data:
            scores = std.get('scores', [])
            if all(isinstance(score, dict) for score in scores):
                score_values = [list(subject.values())[0]for subject in scores]
            else:
                score_values = scores
            averages[std['name']] = (
                sum(score_values)/len(score_values) if score_values else 0
            )
        return averages
