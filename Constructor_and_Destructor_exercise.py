class Person:

    def __init__(self, name, surname, qualification = 1):

        self.name = name

        self.surname = surname

        self.qualification = qualification


    def get_info(self):

        return self.name, self.surname, self.qualification


    def __del__(self):

        print("Goodbye Mr", self.name, self.surname)



person1 = Person("Ani", "Manukyan", 5)

person2 = Person("Ara", "Hovhannisyan", 7)

person3 = Person("Emma", "Watson")

print(person1.get_info())

print(person2.get_info())

print(person3.get_info())



qualification = [person1.qualification, person2.qualification, person3.qualification]

min_q = qualification[0]

for i in qualification:

    if min_q > i:

        min_q = i


if min_q == person1.qualification:

    del person1

elif min_q == person2.qualification:

    del person2

else:

    del person3

input()


'''
qualification = [person1.qualification, person2.qualification, person3.qualification]

min_q = min(qualification)


if person1.qualification == min_q:

    del person1

elif person2.qualification == min_q:

    del person2

else:

    del person3'''


