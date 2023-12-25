class ProblemService:
	
	def __init__(self, repo, validator):
		"""
		The constructor of the ProblemService class.
		Preconditions: repo: an instance of the ProblemRepo class
									 validator: an instance of the ProblemValidator class
		"""
		self.__repo = repo
		self.__validator = validator

	def addProblem(self, newProblem):
		"""
		A function that adds a valid problem in the repo.
		Preconditions: newProblem: a valid instance of the Problem class.
		Post-conditions: -
		Raises: InvalidProblemError: errors
						ProblemRepoError: errors
		"""
		# Check if the problem is valid and if it is not throw an InvalidProblemError
		self.__validator.validateProblem(newProblem)
		# Add the problem and if there's already one with the same id throw a ProblemRepoError
		self.__repo.addProblem(newProblem)
	
	def getProblemById(self, id):
		"""
		A function that returns the problem with the input id.
		Preconditions: id: a string with the following format: int_int
		Post-conditions: an instance of the Problem class.
		Raises: ProblemRepoError: errors
		"""
		return self.__repo.getProblemById(id)
	
	def loadProblems(self):
		"""
		A function that loads the problems from the file in the repo.
		Preconditions: -
		Post-conditions: -
		"""
		self.__repo.loadData()
	
	def saveProblems(self):
		"""
		A function that saves the problems from the repo to the file.
		Preconditions: -
		Post-conditions: -
		"""
		self.__repo.storeData()