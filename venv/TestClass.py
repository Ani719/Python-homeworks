import datetime


class Examination:
    def __init__(self, exam_officers, course_ID, date, location, questions):
        self.exam_officers = exam_officers
        self.course_ID = course_ID
        self.date = date
        self.location = location
        self.questions = questions






m_exam_officers = "Officer 1"
m_course_ID = "exam_0001"
m_date = datetime.datetime(2020, 5, 17)
m_location = "Chaykovsky 34 apt 19"
m_questions = ['q1','q2','q3']

my_exam = Examination(m_exam_officers, m_course_ID, m_date, m_location, m_questions)

my_exam.location = "Tumanyan 10"
print(my_exam.location)


print(my_exam.exam_officers, my_exam.course_ID, my_exam.date, my_exam.location, my_exam.questions)

my_exam.questions =['q4', 'q5', 'q6','q7']
print(my_exam.questions)


