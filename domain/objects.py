class Student:

	def __init__(self, id, name, group):
		"""
		The constructor of the Student class.
		Preconditions: id: a positive integer
									 name: a non-empty string
									 group: a positive integer
		"""
		self.__id = id
		self.__name = name
		self.__group = group
		
	def __str__(self):
		"""
		A function that returns the data formatted when it is printed.
		"""
		return f"{self.__id}, {self.__name}, {self.__group}"
	
	def __eq__(self, otherStudent):
		"""
		A function that overwrites the equality operator.
		Preconditions: otherStudent: an instance of the student class
		Post-conditions: a boolean
		"""
		if self.__id == otherStudent.getId() and self.__name == otherStudent.getName() and self.__group == otherStudent.getGroup():
			return True
		return False
		
	def getId(self):
		"""
		A function that returns the id.
		Preconditions: -
		Post-conditions: a positive integer
		"""
		return self.__id

	def getName(self):
		"""
		A function that returns the name.
		Preconditions: -
		Post-conditions: a string
		"""
		return self.__name

	def getGroup(self):
		"""
		A function that returns the group.
		Preconditions: -
		Post-conditions: a positive integer
		"""
		return self.__group

	def setId(self, newId):
		"""
		A function that sets the id to match newId.
		Preconditions: newId: a positive integer
		Post-conditions: -
		"""
		self.__id = newId

	def setName(self, newName):
		"""
		A function that sets the name to match newName
		Preconditions: newName: a non-empty string
		Post-conditions: -
		"""
		self.__name = newName

	def setGroup(self, newGroup):
		"""
		A function that sets the group to match the newGroup
		Preconditions: newGroup: a positive integer
		Post-conditions: -
		"""
		self.__group = newGroup


class Problem:

	def __init__(self, id, description, deadline):
		"""
		The constructor of the Problem class.
		Preconditions: id: a string with the following format: int_int
									 description: a non-empty string
									 deadline: a string with the following format: mm/dd/yyyy
		"""
		self.__id = id
		self.__description = description
		self.__deadline = deadline
	
	def __str__(self):
		"""
		A function that returns the data formatted when it is printed.
		"""
		return f"{self.__id}, {self.__description}, {self.__deadline}"
	
	def __eq__(self, otherProblem):
		"""
		A function that overwrites the equality operator.
		Preconditions: otherProblem: an instance of the Problem class.
		Post-conditions: a bool
		"""
		if self.__id == otherProblem.getId() and self.__description == otherProblem.getDescription() and self.__deadline == otherProblem.getDeadline():
			return True
		return False
		
	def getId(self):
		"""
		A function that returns the id.
		Preconditions: -
		Post-conditions: a positive string with the following format: int_int
		"""
		return self.__id

	def getDescription(self):
		"""
		A function that returns the description.
		Preconditions: -
		Post-conditions: a non-empty string
		"""
		return self.__description

	def getDeadline(self):
		"""
		A function that returns the  deadline.
		Preconditions: -
		Post-conditions: a non-empty string with the following format: mm/dd/yyyy
		"""
		return self.__deadline

	def setId(self, newId):
		"""
		A function that sets the id the match newId
		Preconditions: newId: a string that has the following format: int_int
		Post-conditions: -
		"""
		self.__id = newId

	def setDescription(self, newDescription):
		"""
		A function that sets the description to match newDescription
		Preconditions: newDescription: a non-empty string
		Post-conditions: -
		"""
		self.__description = newDescription

	def setDeadline(self, newDeadline):
		"""
		A function that sets the deadline to match newDeadline
		Preconditions: newDeadline: a string that has the following format: mm/dd/yyyy
		Post-conditions: -
		"""
		self.__deadline = newDeadline


class Assignment:
	
	def __init__(self, student, problem, mark=0):
		"""
		The constructor of the Assignment class.
		Preconditions: student: an instance of the student class.
									 problem: an instance of the problem class.
									 mark: a positive integer between 0 and 10
		"""
		self.__id = f"{student.getId()}__{problem.getId()}"
		self.__student = student
		self.__problem = problem
		self.__mark = mark
	
	def __str__(self):
		"""
		A function that prints returns the assignment formatted when it is printed.
		"""
		return f"{self.__student}, {self.__problem}, {self.__mark}"
	
	def __eq__(self, otherAssignment):
		"""
		A function that overwrites the equality operator.
		Preconditions: otherAssignment: an instance of the Assignment class.
		Post-conditions: a bool
		"""
		if self.__id == otherAssignment.getAssignmentId() and self.__student == Student(otherAssignment.getStudentId(), otherAssignment.getName(), otherAssignment.getGroup()) and self.__problem == Problem(otherAssignment.getProblemId(), otherAssignment.getDescription(), otherAssignment.getDeadline()):
			return True
		return False
		
	def getAssignmentId(self):
		"""
		A function that returns the id of the assignment.
		Preconditions: -
		Post-conditions: a string with the following format: int__int_int
		"""
		return self.__id
		
	def getStudentId(self):
		"""
		A function that returns the id of the student.
		Preconditions: -
		Post-conditions: a positive integer
		"""
		return self.__student.getId()

	def getName(self):
		"""
		A function that returns the name of the student.
		Preconditions: -
		Post-conditions: a string
		"""
		return self.__student.getName()

	def getGroup(self):
		"""
		A function that returns the group of the student.
		Preconditions: -
		Post-conditions: a positive integer
		"""
		return self.__student.getGroup()

	def getProblemId(self):
		"""
		A function that returns the id of the problem.
		Preconditions: -
		Post-conditions: a string with the following format: int_int
		"""
		return self.__problem.getId()

	def getDescription(self):
		"""
		A function that returns the description of the problem.
		Preconditions: -
		Post-conditions: a string
		"""
		return self.__problem.getDescription()

	def getDeadline(self):
		"""
		A function that returns the deadline of the problem.
		Preconditions: -
		Post-conditions: a string with the following format: mm/dd/yyyy
		"""
		return self.__problem.getDeadline()

	def getMark(self):
		"""
		A function that returns the mark of the problem.
		Preconditions: -
		Post-conditions: a positive integer between 0 and 10
		"""
		return self.__mark
	
	def setStudent(self, newStudent):
		"""
		A function that sets the student to match the newStudent
		Preconditions: newStudent: a valid instance of the Student class.
		Post-conditions: -
		"""
		self.__student = newStudent
		
	def setProblem(self, newProblem):
		"""
		A function that sets the problem to match the newProblem
		Preconditions: newProblem: a valid instance of the Problem class.
		Post-conditions: -
		"""
		self.__problem = newProblem

	def setMark(self, newMark):
		"""
		A function that sets the mark to match newMark
		Preconditions: newMark: a positive integer between 0 and 10
		Post-conditions: -
		"""
		self.__mark = newMark