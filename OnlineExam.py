import logging

logging.basicConfig(
    filename="Exam.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Exam:

    pass_marks = 40
    total_questions = 50
    active_students = []

    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.correct_attempts = 0

    def start_exam(self):
        if self.student_id in Exam.active_students:
            logging.warning("Exam already started for %s", self.student_name)
            return

        Exam.active_students.append(self.student_id)
        logging.info("Exam started for %s", self.student_name)

    def submit_exam(self, correct_attempts):
        if self.student_id not in Exam.active_students:
            logging.warning("Exam not started yet for %s", self.student_name)
            return

        if correct_attempts < 0 or correct_attempts > Exam.total_questions:
            logging.error("Invalid correct attempts for %s", self.student_name)
            return

        self.correct_attempts = correct_attempts
        Exam.active_students.remove(self.student_id)
        logging.info("Exam submitted by %s", self.student_name)

    def calculate_score(self):
        if self.correct_attempts == 0:
            logging.warning("No submission found for %s", self.student_name)
            return

        percentage = (self.correct_attempts / Exam.total_questions) * 100
        result = "PASS" if percentage >= Exam.pass_marks else "FAIL"

        logging.info("Student: %s | Correct: %d | Percentage: %.2f | Result: %s",
                     self.student_name, self.correct_attempts, percentage, result)

    @classmethod
    def update_pass_marks(cls, new_marks):
        cls.pass_marks = new_marks
        logging.info("Pass marks updated to %d", cls.pass_marks)
s1 = Exam("Padmasri",101)
s1.start_exam()
s1.submit_exam(35)
s1.calculate_score()

s2 = Exam("Ravi",102)
s2.calculate_score()
s2.start_exam()
s2.submit_exam(10)
s2.calculate_score()

s1.update_pass_marks(60)
s2.calculate_score()
