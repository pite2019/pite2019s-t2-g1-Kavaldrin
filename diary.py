
class Student:

	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.scores = {}


class SchoolClass:

	def __init__(self,name_of_class):
		self.name = name_of_class
		self.attendance = {}
		self.students = []

	def add_students(*students):
		self.students = [student for student in students]


class Diary:
	def __init__(self):
		self.classes = {}

	def add_school_class(school_class):
		self.classes[school_class.name] = school_class

	def add_students_to_school_class(class_name, *students):
		if class_name in self.classes:
			self.classes[class_name].add_students(students)

	def add_score_for_student(student, class_name, score):
		if class_name in self.classes:
			if student in self.classes[class_name].students:
				self.classes[class_name].students[student].scores[(class_name)].append(score)