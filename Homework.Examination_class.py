import datetime


class Examination:
    def __init__(self, exam_officer, course_ID, date, location, questions):
        self.exam_officer = exam_officer
        self.course_ID = course_ID
        self.date = date
        self.location = location
        self.questions = questions


     #methods
    def print_exam_info(self):
        print(my_exam.exam_officer, my_exam.course_ID, my_exam.date, my_exam.location, my_exam.questions)

    def change_location(self, new_location):
        self.location = new_location
        print(my_exam.exam_officer, my_exam.course_ID, my_exam.date, my_exam.location, my_exam.questions)


    def postpone_exam(self, new_date):
        self.date = new_date
        print(my_exam.exam_officer, my_exam.course_ID, new_date, my_exam.location, my_exam.questions)


    def change_questions_list(self, new_questions_list):
        self.questions =new_questions_list
        print(my_exam.exam_officer, my_exam.course_ID, my_exam.date, my_exam.location, my_exam.questions)


m_exam_officer = "Officer 1"
m_course_ID = "exam_0001"
m_date = datetime.datetime(2020, 5, 17)
m_location = "Chaykovsky 34 apt 19"
m_questions = ['q1','q2','q3']


my_exam = Examination(m_exam_officer, m_course_ID, m_date, m_location, m_questions)
my_exam.print_exam_info()
my_exam.change_location("Khorenaci 20")
my_exam.postpone_exam(datetime.datetime(2020, 9, 2))
my_exam.change_questions_list(['q4', 'q5', 'q5', 'q6', 'q7'])
