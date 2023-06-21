class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lec = {}

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades_lec:
                lecture.grades_lec[course] += [grade]
            else:
                lecture.grades_lec[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_st(self):
        summ = 0
        length = 0
        val = self.grades.values()
        val_list = list(val)
        for i in val_list:
            for j in i:
                summ += j
                length += 1
        result = round(summ / length, 2)
        return result

    def lt(self, other):
        return self.average_grade_st() < other.average_grade_st()

    def __str__(self):
        return (f"Имя: {self.name}\n Фамилия: {self.surname}\n "
                f"Средняя оценка за домашние задания: {self.average_grade_st()}\n "
                f"Курсы в процессе изучения: {self.courses_in_progress}\n"
                f" Завершённые курсы: {self.finished_courses}")


class Lecturer(Mentor):
    def average_grade_lec(self):
        summ = 0
        length = 0
        val = self.grades_lec.values()
        val_list = list(val)
        for i in val_list:
            for j in i:
                summ += j
                length += 1
        result = round(summ / length, 2)
        return result

    def __str__(self):
        return (f"Имя: {self.name}\n Фамилия: {self.surname}\n "
                f"Средняя оценка за лекции: {self.average_grade_lec()}")

    def lt(self, other):
        return self.average_grade_lec() < other.average_grade_lec()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n Фамилия: {self.surname}")

def get_avg_lect_grade(lecturers, course):
    summ = 0
    for lecturer in lecturers:
        summ += sum(lecturer.grades[course]) / len(lecturer.grades[course])
    return summ / len(lecturers)

def get_avg_lect_grade(lecturers, course):
    summ = 0
    for lecturer in lecturers:
        summ += sum(lecturer.grades[course]) / len(lecturer.grades[course])
    return sum([sum(lecturer.grades[course]) / len(lecturer.grades[course]) for lecturer in lecturers]) / len(lecturers)


student_1 = Student('Lina', 'Nova', 'woman')
student_1.courses_in_progress = ['Python', 'Java Script', 'C++']
student_1.finished_courses = ['Git']

student_2 = Student('Michael', 'Torres', 'man')
student_2.courses_in_progress = ['Python', 'Java Script', 'C++']
student_2.finished_courses = ['C#']

reviewer_1 = Reviewer('Din', 'Colins')
reviewer_1.courses_attached = ['Python', 'Java Script', 'C++']

print(f'Проверяющий: {reviewer_1.name} {reviewer_1.surname}\nВедёт курсы: {", ".join(reviewer_1.courses_attached)}\n')

reviewer_2 = Reviewer('Kas', 'Kroow')
reviewer_2.courses_attached = ['Python', 'Java Script', 'C++']

print(f'Проверяющий: {reviewer_2.name} {reviewer_2.surname}\nВедёт курсы: {", ".join(reviewer_2.courses_attached)}\n')

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java Script', 8)
reviewer_1.rate_hw(student_1, 'C++', 7)
#print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}')

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Java Script', 10)
reviewer_2.rate_hw(student_1, 'C++', 8)
print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}\n')

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Java Script', 6)
reviewer_1.rate_hw(student_2, 'C++', 10)
#print(f'Оценки студента: {student_2.name} {student_2.surname}\n{student_2.grades}')

reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Java Script', 9)
reviewer_2.rate_hw(student_2, 'C++', 7)
print(f'Оценки студента: {student_2.name} {student_2.surname}\n{student_2.grades}\n')

lecture_1 = Lecturer('Klara', 'Sam')
lecture_1.courses_attached = ['Python', 'Java Script', 'C++']

lecture_2 = Lecturer('Regina', 'Wesly')
lecture_2.courses_attached = ['Python', 'Java Script', 'C++']

student_1.rate_lecturer(lecture_1, 'Python', 1)
student_1.rate_lecturer(lecture_1, 'Java Script', 2)
student_1.rate_lecturer(lecture_1, 'C++', 3)

student_2.rate_lecturer(lecture_1, 'Python', 7)
student_2.rate_lecturer(lecture_1, 'Java Script', 8)
student_2.rate_lecturer(lecture_1, 'C++', 9)

print(f'Оценки лектору: {lecture_1.name} {lecture_1.surname}\n{lecture_1.grades_lec}\n')

student_1.rate_lecturer(lecture_2, 'Python', 4)
student_1.rate_lecturer(lecture_2, 'Java Script', 5)
student_1.rate_lecturer(lecture_2, 'C++', 6)

student_2.rate_lecturer(lecture_2, 'Python', 10)
student_2.rate_lecturer(lecture_2, 'Java Script', 1)
student_2.rate_lecturer(lecture_2, 'C++', 2)

print(f'Оценки лектору: {lecture_2.name} {lecture_2.surname}\n{lecture_2.grades_lec}\n')

print(f"Проверяющий 1: \n", reviewer_1)
print(f"Проверяющий 2: \n", reviewer_2)

#print(f'Средняя оценка студ 1:', student_1.average_grade_st(), "\n")
#print(f'Средняя оценка студ 2:', student_2.average_grade_st(), "\n")

#print(f"Средняя оценка лек 1:", lecture_1.average_grade_lec(), "\n")
#print(f"Средняя оценка лек 2:", lecture_2.average_grade_lec(), "\n")

print(f"Студент 1: \n", student_1)
print(f"Студент 2: \n", student_2)

print(f"Лектор 1: \n", lecture_1)
print(f"Лектор 2: \n", lecture_2)

print(student_1.lt(student_2))
print(student_2.lt(student_1))

print(lecture_1.lt(lecture_2))
print(lecture_2.lt(lecture_1))

print(get_avg_lect_grade([lecture_1], 'Python'))
print(get_avg_lect_grade([lecture_2], 'Python'))