class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_st(self):
        grade_list = []
        for v in self.grades.items():
            for i in v:
                grade_list.append(i)
        result = round(sum(grade_list) / len(grade_list), 2)
        return result

    def lt(self, other):
        return self.average_grade_st() < other.average_grade_st()

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n "
                f"Средняя оценка за домашние задания: {self.average_grade_st()}\n Курсы в процессе изучения: {self.courses_in_progress}\n"
                f" Завершённые курсы: {self.add_courses()}")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades_lec = {}
    def average_grades(self):
        grades_list = []
        for course, grade in self.grades_lec.items():
            grades_list.append(grade)
        average = sum(grades_list) / len(grades_list)
        return average

    def __str__(self):
        return (f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_grades()}")

    def lt(self, other):
        return self.average_grades() < other.average_grades()


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

student_1 = Student('Lina', 'Nova', 'woman')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java Script']
student_1.courses_in_progress += ['C++']

student_2 = Student('Michael', 'Torres', 'man')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java Script']
student_2.courses_in_progress += ['C++']

reviewer_1 = Reviewer('Din', 'Colins')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java Script']
reviewer_1.courses_attached += ['C++']
print(f'Проверяющий: {reviewer_1.name} {reviewer_1.surname}\nВедёт курсы: {", ".join(reviewer_1.courses_attached)}\n')

reviewer_2 = Reviewer('Kas', 'Kroow')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java Script']
reviewer_2.courses_attached += ['C++']
print(f'Проверяющий: {reviewer_2.name} {reviewer_2.surname}\nВедёт курсы: {", ".join(reviewer_2.courses_attached)}\n')

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java Script', 8)
reviewer_1.rate_hw(student_1, 'C++', 7)
print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}')

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Java Script', 10)
reviewer_2.rate_hw(student_1, 'C++', 8)
print(f'Оценки студента: {student_1.name} {student_1.surname}\n{student_1.grades}')

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Java Script', 6)
reviewer_1.rate_hw(student_2, 'C++', 10)
print(f'Оценки студента: {student_2.name} {student_2.surname}\n{student_2.grades}')

reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Java Script', 9)
reviewer_2.rate_hw(student_2, 'C++', 7)
print(f'Оценки студента: {student_2.name} {student_2.surname}\n{student_2.grades}')

#list_stud = [student_1, student_2]
#print(Student.average_grade_st(list_stud))

lecture_1 = Lecturer('Klara', 'Sam')
lecture_1.courses_attached += ['Python']
lecture_1.courses_attached += ['Java Script']
lecture_1.courses_attached += ['C++']

lecture_2 = Lecturer('Regina', 'Wesly')
lecture_2.courses_attached += ['Python']
lecture_2.courses_attached += ['Java Script']
lecture_2.courses_attached += ['C++']

student_1.rate_lecturer(lecture_1, 'Python', 5)
student_1.rate_lecturer(lecture_1, 'Java Script', 8)
student_1.rate_lecturer(lecture_1, 'C++', 10)

student_1.rate_lecturer(lecture_2, 'Python', 7)
student_1.rate_lecturer(lecture_2, 'Java Script', 10)
student_1.rate_lecturer(lecture_2, 'C++', 9)

student_2.rate_lecturer(lecture_1, 'Python', 7)
student_2.rate_lecturer(lecture_1, 'Java Script', 10)
student_2.rate_lecturer(lecture_1, 'C++', 9)

student_2.rate_lecturer(lecture_2, 'Python', 7)
student_2.rate_lecturer(lecture_2, 'Java Script', 10)
student_2.rate_lecturer(lecture_2, 'C++', 9)

print(f'Оценки лектору: {lecture_1.name} {lecture_1.surname}\n{lecture_1.grades}')
print(f'Оценки лектору: {lecture_2.name} {lecture_2.surname}\n{lecture_2.grades}')


print(f"{student_1.name} {student_1.surname} оценки:", student_1.grades)
print(f"{student_2.name} {student_2.surname} оценки:", student_2.grades)

print(f"Студент 1: \n", student_1)
print(f"Студент 2: \n", student_2)

print(f"Проверяющий 1: \n", reviewer_1)

print(f"Лектор 1: \n", lecture_1)