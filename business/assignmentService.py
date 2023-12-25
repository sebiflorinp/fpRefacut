from utils.errors import AssignmentRepoError, AssignmentServiceError, StudentRepoError


class AssignmentService:
	
	def __init__(self, repo, validator, studentRepo, problemRepo, studentValidator, problemValidator):
		"""
		The constructor of the AssignmentService class.
		Preconditions: repo: an instance of the AssignmentRepo class.
									 validator: an instance of the AssignmentValidator class.
									 studentRepo: an instance of the StudentRepo class.
									 problemRepo: an instance of the ProblemRepo class.
									 studentValidator: an instance of the StudentValidator class.
									 problemValidator: an instance of the ProblemValidator class.
		"""
		self.__repo = repo
		self.__validator = validator
		self.__studentRepo = studentRepo
		self.__problemRepo = problemRepo
		self.__studentValidator = studentValidator
		self.__problemValidator = problemValidator
	
	def addAssignment(self, newAssignment):
		"""
		A function that adds newAssignment in the repo.
		Preconditions: newAssignment: a valid instance of the Assignment class.
		Post-conditions: -
		Raises: InvalidAssignmentError: errors
						AssignmentRepoError: errors
		"""
		# Check if the assignment is valid and if it isn't throw an InvalidAssignmentError
		self.__validator.validateAssignment(newAssignment)
		# Add the assignment or throw an AssignmentRepoError if there's another assignment with the same id
		self.__repo.addAssignment(newAssignment)
	
	def markAssignment(self, assignmentId, mark):
		"""
		A function that changes the mark of the assignment to the input one.
		Preconditions: assignmentId: a string with the following format: int__int_int
									 mark: a positive integer between 1 and 10
		Post-conditions: -
		Raises: AssignmentServiceError: the id is invalid
																		the mark is invalid
						AssignmentRepoError: errors
		"""
		if len(assignmentId.split("__")) != 2:
			raise AssignmentServiceError("the id is invalid")
		if len(assignmentId.split("__")[1].split("_")) != 2:
			raise AssignmentServiceError("the id is invalid")
		try:
			int(assignmentId.split("__")[0])
			int(assignmentId.split("__")[1].split("_")[0])
			int(assignmentId.split("__")[1].split("_")[1])
		except ValueError:
			raise AssignmentServiceError("the id is invalid")
		try:
			int(mark)
		except ValueError:
			raise AssignmentServiceError("the mark is invalid")
		if not 1 <= int(mark) <= 10:
			raise AssignmentServiceError("the mark is invalid")
		self.__repo.markAssignment(assignmentId, mark)
	
	def getAll(self):
		"""
		A function that returns a list with all assignments.
		Preconditions: -
		Post-conditions: a list with instances of the Assignment class.
		"""
		return self.__repo.getAll()
	
	def deleteStudent(self, id):
		"""
		A function that deletes the student with a given id and the assignments of that student.
		Preconditions: id: a positive integer
		Post-conditions:
		Raises: AssignmentRepoError: errors
						AssignmentServiceRepo: the id is invalid
		"""
		# Delete the student.
		try:
			int(id)
		except ValueError:
			raise AssignmentServiceError("the id is invalid")
		self.__studentRepo.deleteStudentById(int(id))
		# Delete problems.
		try:
			self.__repo.deleteByStudentId(int(id))
		except AssignmentRepoError:
			pass
	
	def deleteProblem(self, id):
		"""
		A function that deletes the problem with the given id and the assignments that have the deleted problem.
		Preconditions: id: a string with the following format: int_int
		Post-conditions: -
		Raises: AssignmentRepoError: errors
		"""
		# Delete the problem
		self.__problemRepo.deleteProblemById(id)
		# Delete the assignments with the deleted problem.
		try:
			self.__repo.deleteByProblemId(id)
		except AssignmentRepoError:
			pass
	
	def updateStudent(self, id, updatedStudent):
		"""
		A function that updates the student that has the input id to match updatedStudent and updates the assigments given
		to that student.
		Preconditions: id: a positive integer
									 updatedStudent: an instance of the Student class.
		Post-conditions: - 
		Raises: StudentRepoError: errors
						AssignmentServiceError: the id is invalid
						InvalidStudentError: errors
		"""
		try:
			int(id)
		except ValueError:
			raise AssignmentServiceError("the id is invalid")
		self.__studentValidator.validateStudent(updatedStudent)
		#Update the student or throw an error if there is no student with the input id.
		self.__studentRepo.updateStudentById(int(id), updatedStudent)
		#Update all problems 
		try:
			self.__repo.updateAssignmentByStudent(int(id), updatedStudent)
		except AssignmentRepoError:
			pass
	
	def updateProblem(self, id, updatedProblem):
		"""
		A function that updates the problem with the input id to match the updatedProblem and all assignments that contain
		the updated problem.
		Preconditions: id: a string with the following format: int_int
									 updatedProblem: an instance of the Problem class
		Post-conditions: -
		Raises: InvalidProblemError: errors
					  AssignmentServiceError: the id is invalid
		"""
		if len(id.split("_")) != 2:
			raise AssignmentServiceError("the id is invalid")
		try:
			int(id.split("_")[0])
			int(id.split("_")[1])
		except ValueError:
			raise AssignmentServiceError("the id is invalid")
		self.__problemValidator.validateProblem(updatedProblem)
		self.__problemRepo.updateProblemById(id, updatedProblem)
		self.__repo.updateAssignmentByProblem(id, updatedProblem)
	
	def loadAssignments(self):
		"""
		A function that loads the assignments from the file in the repo.
		Preconditions: -
		Post-conditions: -
		"""
		self.__repo.loadData()
		
	def saveAssignments(self):
		"""
		A function that saves the assignment from the repo to the file.
		Preconditions: -
		Post-conditions: -
		"""
		self.__repo.storeData()
	
	def returnSortedMarks(self, problemId):
		"""
		A function that returns a list that contains the student name and mark at a given problem.
		Preconditions: problemId: a string with the following format: int_int
		Post-conditions: a list with lists made of a string and an int
		Raises: AssignmentServiceError: the id is invalid
																		there's no assignment with the given problem
																		there's no problem with the given id
		"""
		if len(problemId.split("_")) != 2:
			raise AssignmentServiceError("the id is invalid")
		try:
			int(problemId.split("_")[0])
			int(problemId.split("_")[1])
		except ValueError:
			raise AssignmentServiceError("the id is invalid")
		thereIsAProblem = False
		for problem in self.__problemRepo.getAll():
			if problem.getId() == problemId:
				thereIsAProblem = True
		if not thereIsAProblem:	
			raise AssignmentServiceError("there's no problem with the given id")
		assignments = self.__repo.getAll()
		assignments = list(filter(lambda assignment: assignment.getProblemId() == problemId and (assignment.getMark()) != 0 , assignments))
		if len(assignments) == 0:
			raise AssignmentServiceError("there's no assignment with the given problem")
		assignments.sort(key=lambda assignment: assignment.getName(), reverse=False)
		assignments.sort(key=lambda assignment: int(assignment.getMark()), reverse=True)
		return [[assignment.getName(), assignment.getMark()] for assignment in assignments]
	
	def getStudentsWhoFail(self):
		"""
		A function that returns the students whose average mark is below 5 and their average mark.
		Preconditions: -
		Post-conditions: a list of lists of 2 elements: 1 student name, 2 student mark
		Raises: there are no marked assignments
		"""
		assignments = self.__repo.getAll()
		assignments = list(filter(lambda assignment: assignment.getMark() != 0, assignments))
		studentsAndMarks = {}
		for assignment in assignments:
			if int(assignment.getStudentId()) in studentsAndMarks:
				studentsAndMarks[int(assignment.getStudentId())].append(int(assignment.getMark()))
			else:
				studentsAndMarks[int(assignment.getStudentId())] = [int(assignment.getMark())]
		for key in studentsAndMarks:
			studentsAndMarks[key] = sum(studentsAndMarks[key]) / len(studentsAndMarks[key])
		listToReturn = []
		for key in studentsAndMarks:
			if studentsAndMarks[key] < 5:
				listToReturn.append([self.__studentRepo.getStudentById(int(key)).getName(),studentsAndMarks[key]])
		return listToReturn