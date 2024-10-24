class StudentStatistics:
    def __init__(self, data):
        self.data = data.get('students', [])

    def calculate_average_score(self):
        """Вычесление среднего балла каждого студента."""
        averages = {}
        for std in self.data:
            scores = std.get('scores', [])
            averages[std['name']] = sum(scores)/len(scores) if scores else 0
        return averages
