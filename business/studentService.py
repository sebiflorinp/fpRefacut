class StudentService:
	
	def __init__(self, repo, validator):
		"""
		The constructor of the StudentService class.
		Preconditions: repo: an instance of the StudentRepo class.
									 validator: an instance of the StudentValidator class.
		"""
		self.__repo = repo
		self.__validator = validator
	
	def addStudent(self, newStudent):
		"""
		A function that adds a valid student in the repo.
		Preconditions: newStudent: a valid instance of the Student class.
		Post-conditions: -
		Raises: InvalidStudentError: errors
						StudentRepoError: errors
		"""
		# Check if the student is valid and if it isn't throw an InvalidStudentError
		self.__validator.validateStudent(newStudent)
		# Add the student or if already is one throw a StudentRepoError
		self.__repo.addStudent(newStudent)
	
	def getStudentById(self, id):
		"""
		A function that returns a student with the input id.
		Preconditions: id: a positive integer
		Post-conditions: an instance of the Student class.
		Raises: StudentRepoError: errors
		"""
		return self.__repo.getStudentById(id)
	
	def updateStudentById(self, id, newStudent):
		"""
		A function that updates the student with the input id to match the newStudent.
		Preconditions: id: a positive integer
									 newStudent: a valid instance of the Student class.
		Post-conditions: -
		Raises: InvalidStudentError: errors
						StudentRepoError: errors
		"""
		# Validate the newStudent and if it is invalid throw an InvalidStudentError.
		self.__validator.validateStudent(newStudent)
		# Update the student with the input id or throw a StudentRepoError if the update creates duplicates
		self.__repo.updateStudentById(id, newStudent)
	
	def loadStudents(self):
		"""
		A function that loads the students from the file in the repo.
		Preconditions: -
		Post-conditions: -
		"""
		self.__repo.loadData()
	
	def saveStudents(self):
		"""
		A function that saves the students in the repo in a file.
		Preconditions: -
		Post-conditions: -
		"""
		self.__repo.storeData()