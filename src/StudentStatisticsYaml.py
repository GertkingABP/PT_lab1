class StudentStatisticsYaml:
    def __init__(self, data):
        self.data = data if isinstance(data, dict) else {'students': data}

    def calculate_average_score(self):
        """Расчет среднего балла для каждого студента"""
        averages = {}
        for student in self.data.get('students', []):
            if isinstance(student['scores'][0], dict):
                scores = [score for subject in student['scores']
                          for score in subject.values()]
            else:
                scores = student['scores']
            averages[student['name']] = (sum(scores) /
                                         len(scores) if scores else 0)
        return averages

    def find_student_with_min_scores(self, min_scr=76):
        """Поиск студента, набравшего минимум min_scr по 3 дисциплинам"""
        for student in self.data.get('students', []):
            scores = [score for subject in student['scores']
                      for score in (subject.values()
                      if isinstance(subject, dict) else [subject])]
            qualifying_scores = [score for score in scores if score >= min_scr]
            if len(qualifying_scores) >= 3:
                return student['name']
        return "No student found with the min required scores."

    def find_high_achievers(self, high_score=90):
        """Находит студентов, у которых каждый балл равен или превышает 90."""
        high_achievers = []
        for student in self.data.get('students', []):
            scores = [score for subject in student['scores']
                      for score in (subject.values()
                      if isinstance(subject, dict)
                      else [subject])]
            if all(score >= high_score for score in scores):
                high_achievers.append(student['name'])
        return high_achievers if high_achievers else "\nNo high achiv-s found"

    def find_low_performers(self, low_score=61):
        """Находит студентов, у которых каждый балл ниже low_score."""
        low_performers = []
        for student in self.data.get('students', []):
            scores = [score for subject in student['scores']
                      for score in (subject.values()
                      if isinstance(subject, dict)
                      else [subject])]
            if all(score < low_score for score in scores):
                low_performers.append(student['name'])
        return low_performers if low_performers else "\nNo low perform-s found"
