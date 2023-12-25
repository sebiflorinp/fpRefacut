from domain.objects import Student, Problem, Assignment
from utils.errors import StudentRepoError, ProblemRepoError, AssignmentRepoError


class StudentRepo:
	
	def __init__(self):
		"""
		The constructor of the StudentRepo class.
		Preconditions: -
		"""
		self.__repo = {}

	def getStudentById(self, id):
		"""
		A function that returns the student with the input id.
		Preconditions: id: a positive integer
		Post-conditions: an instance of the Student object.
		Raises: StudentRepoError: there is no student with the input 
															the input id is not a valid id
		"""
		try:
			int(id)
		except ValueError:
			raise StudentRepoError("the input id is not a valid id")
		if int(id) not in self.__repo:
			raise StudentRepoError("there is no student with the input id")
		return self.__repo[int(id)]
		

	def getAll(self):
		"""
		A function that returns a list with the students from the repo.
		Preconditions: -
		Post-conditions: a list with instance of the Student class.
		"""
		return [self.__repo[key] for key in self.__repo]

	def addStudent(self, newStudent):
		"""
		A function that adds newStudent in the repo.
		Preconditions: newStudent: an instance of the Student class.
		Post-conditions: -
		Raises: StudentRepoError: there is already a student with the id of newStudent
		"""
		if int(newStudent.getId()) in self.__repo:
			raise StudentRepoError("there is already a student with the id of newStudent")
		newStudent.setId(int(newStudent.getId()))
		self.__repo[int(newStudent.getId())] = newStudent

	def deleteStudentById(self, id):
		"""
		A function that deletes the student that has the input id.
		Preconditions: id: a positive integer
		Post-conditions: -
		Raises: StudentRepoError: there is no student with the input id.
		"""
		if id not in self.__repo:
			raise StudentRepoError("there is no student with the input id.")
		del self.__repo[id]

	def updateStudentById(self, id, updatedStudent):
		"""
		A function that updates the student with the input id to match updatedStudent.
		Preconditions: id: a positive integer
									 updatedStudent: an instance of the Student class
		Post-conditions: -
		Raises: StudentRepoError: there are no students with the input id
															the update operation would create duplicates in the repo
															the id is invalid
						InvalidStudentError: errors
		"""
		try:
			int(id)
		except ValueError:
			raise StudentRepoError("the id is invalid")
		
		if int(id) not in self.__repo:
			raise StudentRepoError("there are no students with the input id")
		if int(id) != updatedStudent.getId() and int(updatedStudent.getId()) in self.__repo:
			raise StudentRepoError("the update operation would create duplicates in the repo")
		del self.__repo[int(id)]
		self.__repo[int(updatedStudent.getId())] = updatedStudent

	def storeData(self):
		"""
		A function that stores the students from the repo in a file.
		Preconditions: -
		Post-conditions: -
		"""
		with open("files/students.txt", "w") as file:
			for key in self.__repo:
				student = self.__repo[key]
				file.write(f"{student.getId()}, {student.getName()}, {student.getGroup()}\n")

	def loadData(self):
		"""
		A function that loads the students from a file into the repo.
		Preconditions: -
		Post-conditions: -
		"""
		with open("files/students.txt", "r") as file:
			data = file.readline().strip().split(", ")
			while len(data) == 3:
				id = int(data[0])
				name = data[1]
				group = int(data[2])
				student = Student(id, name, group)
				self.__repo[id] = student
				data = file.readline().strip().split(", ")


class ProblemRepo:

	def __init__(self):
		"""
		The constructor of the ProblemRepo class.
		"""
		self.__repo = {}

	def getProblemById(self, id):
		"""
		A function that returns the problem with the input id.
		Preconditions: id: a string with the following format: int_int
		Post-conditions: an instance of the Problem class
		Raises: ProblemRepoError: there is no problem with the input id
															the id is invalid
		"""
		if len(id.split("_")) != 2:
			raise ProblemRepoError("the id is invalid")
		try:
			int(id.split("_")[0])
			int(id.split("_")[1])
		except ValueError:
			raise ProblemRepoError("the id is invalid")
		if id not in self.__repo:
			raise ProblemRepoError("there is no problem with the input id")
		return self.__repo[id]


	def getAll(self):
		"""
		A function that returns a list with all the problems.
		Preconditions: -
		Post-conditions: a list with instance of Problem class
		"""
		return [self.__repo[key] for key in self.__repo]
	
	def addProblem(self, newProblem):
		"""
		A function that adds newProblem in the repo.
		Preconditions: newProblem: an instance of the Problem class.
		Post-conditions: -
		Raises: ProblemRepoError: there is already a problem with the id of newProblem
		"""
		if newProblem.getId() in self.__repo:
			raise ProblemRepoError("there is already a problem with the id of newProblem")
		self.__repo[newProblem.getId()] = newProblem

	def deleteProblemById(self, id):
		"""
		A function that deletes the Problem with the input id.
		Preconditions: id: a string with the following format: int_int
		Post-conditions: -
		Raises: ProblemRepoError: there is no problem with the input id
															the id is invalid
		"""
		if len(id.split("_")) != 2:
			raise ProblemRepoError("the id is invalid")
		try:
			int(id.split("_")[0])
			int(id.split("_")[1])
		except ValueError:
			raise ProblemRepoError("the id is invalid")
		if id not in self.__repo:
			raise ProblemRepoError("there is no problem with the input id")
		del self.__repo[id]

	def updateProblemById(self, id, updatedProblem):
		"""
		A function that updates the problem with the input id to match updatedProblem.
		Preconditions: id: a string with the following format: int_int
									 updatedProblem: an instance of the Problem class.
		Post-conditions: -
		Raises: ProblemRepoError: there is no problem with the input id
															the update operation would create duplicates
		"""
		if id not in self.__repo:
			raise ProblemRepoError("there is no problem with the input id")
		if id != updatedProblem.getId() and updatedProblem.getId() in self.__repo:
			raise ProblemRepoError("the update operation would create duplicates")
		del self.__repo[id]
		self.__repo[updatedProblem.getId()] = updatedProblem

	def storeData(self):
		"""
		A function that stores all the data in the repo in a file.
		Preconditions: -
		Post-conditions: -
		"""
		with open("files/problems.txt", "w") as file:
			for key in self.__repo:
				problem = self.__repo[key]
				file.write(f"{problem.getId()}, {problem.getDescription()}, {problem.getDeadline()}\n")

	def loadData(self):
		"""
		A function that loads all data stored in a file to the repo.
		Preconditions: -
		Post-conditions: -
		"""
		with open("files/problems.txt", "r") as file:
			data = file.readline().strip().split(", ")
			while len(data) == 3:
				id = data[0]
				description = data[1]
				deadline = data[2]
				problem = Problem(id, description, deadline)
				self.__repo[id] = problem
				data = file.readline().strip().split(", ")


class AssignmentRepo:
	
	def __init__(self):
		"""
		The constructor of the AssignmentRepo class.
		Preconditions: studentRepo: an instance of the StudentRepo class
									 problemRepo: an instance of the ProblemRepo class
		"""
		self.__repo = {}

	def getAll(self):
		"""
		A function that returns a list with all assignments in the repo.
		Preconditions: -
		Post-conditions: a list with instances of Assignment class.
		"""
		return [self.__repo[key] for key in self.__repo]
	
	def addAssignment(self, newAssignment):
		"""
		A function that adds a new assignment in the repo.
		Preconditions: newAssignment: an instance of the Assignment class.
		Post-conditions: -
		Raises: AssignmentRepoError: there is already an assignment with the id of newAssignment
		"""
		if newAssignment.getAssignmentId() in self.__repo:
			raise AssignmentRepoError("there is already an assignment with the id of newAssignment")
		self.__repo[newAssignment.getAssignmentId()] = newAssignment
		
	def markAssignment(self, assignmentId, mark):
		"""
		A function that changes the mark of the assignment with the assignmentId to mark.
		Preconditions: assignmentId: a string with the following format: int__int_int
									 mark: a positive integer between 1 and 10
		Preconditions: -
		Raises: AssignmentRepoError: there is no problem with the input id
		"""
		if assignmentId not in self.__repo:
			raise AssignmentRepoError("there is no problem with the input id")
		self.__repo[assignmentId].setMark(mark)
	
	def deleteByStudentId(self, id):
		"""
		A function that deletes all assignments given to the student with the input id.
		Preconditions: id: a positive integer
		Post-conditions: -
		Raises: AssignmentRepoError: there are no assignments given to a student with the input id.
		"""
		keysToDelete = []
		for key in self.__repo:
			if int(self.__repo[key].getStudentId()) == int(id):
				keysToDelete.append(key)
		if len(keysToDelete) == 0:
			raise AssignmentRepoError("there are no assignments given to a student with the input id.")
		for key in keysToDelete:
			del self.__repo[key]
	
	def deleteByProblemId(self, id):
		"""
		A function that deletes all assignments that have the problem with the input id.
		Preconditions: id: string with the following format: int_int
		Post-conditions: -
		Raises: AssignmentRepoError: there are no assignments with the problem that has the input id
		"""
		hasDeletedSomething = False
		keysToDelete = []
		for key in self.__repo:
			if self.__repo[key].getProblemId() == id:
				keysToDelete.append(key)
				hasDeletedSomething = True
		for key in keysToDelete:
			del self.__repo[key]
		if not hasDeletedSomething:
			raise AssignmentRepoError("there are no assignments with the problem that has the input id")
	
	def updateAssignmentByStudent(self, studentId, updatedStudent):
		"""
		A function that updates the assignments that have a student with studentId so that the student matches updatedStudent
		Preconditions: studentId: a positive integer
									 updatedStudent: an instance of the Student class.
		Post-conditions: -
		Raises: AssignmentRepoError: there is no student with the input id
																 the id is invalid
		"""
		keysToUpdate = []
		try:
			int(studentId)
		except ValueError:
			raise AssignmentRepoError("the id is invalid")
		for key in self.__repo:
			if int(self.__repo[key].getStudentId()) == int(studentId):
				keysToUpdate.append(key)
		if len(keysToUpdate) == 0:
			raise AssignmentRepoError("there is no student with the input id")
		for key in keysToUpdate:
			self.__repo[key].setStudent(updatedStudent)
	
	def updateAssignmentByProblem(self, problemId, updatedProblem):
		"""
		A function that updates the assignments that have the problem with the input id in order to match the updatedProblem.
		Preconditions: problemId: a string with the following format: int_int
									 updatedProblem: an instacen of the Problem class.
		Post-conditions: -
		Raises: there is no problem with the input id
		"""
		keysToUpdate = []
		for key in self.__repo:
			if self.__repo[key].getProblemId() == problemId:
				keysToUpdate.append(key)
		if len(keysToUpdate) == 0:
			raise AssignmentRepoError("there is no problem with the input id")
		for key in keysToUpdate:
			self.__repo[key].setProblem(updatedProblem)
		

	def storeData(self):
		"""
		A function that stores the assignments in the repo in a file.
		Preconditions: -
		Post-conditions: -
		"""
		with open("files/assignments.txt", "w") as file:
			for key in self.__repo:
				studentId = self.__repo[key].getStudentId()
				name = self.__repo[key].getName()
				group = self.__repo[key].getGroup()
				problemId = self.__repo[key].getProblemId()
				description = self.__repo[key].getDescription()
				deadline = self.__repo[key].getDeadline()
				mark = self.__repo[key].getMark()
				file.write(f"{studentId}, {name}, {group}, {problemId}, {description}, {deadline}, {mark}\n")

	def loadData(self):
		"""
		A function that loads data from a file.
		Preconditions: -
		Post-conditions: -
		"""
		with open("files/assignments.txt", "r") as file:
			data = file.readline().strip().split(", ")
			while len(data) == 7:
				studentId = int(data[0])
				name = data[1]
				group = int(data[2])
				student = Student(studentId, name, group)
				problemId = data[3]
				description = data[4]
				deadline = data[5]
				problem = Problem(problemId, description, deadline)
				mark = int(data[6])
				assignment = Assignment(student, problem, mark)
				self.__repo[assignment.getAssignmentId()] = assignment
				data = file.readline().strip().split(", ")