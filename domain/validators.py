from utils.errors import InvalidStudentError, InvalidProblemError, InvalidAssignmentError

class StudentValidator:
	
	def validateStudent(self, student):
		"""
		A function that checks if the received student is a valid instance of the Student class.
		Preconditions: student: an instance of the Student class.
		Post-conditions: -
		Raises: InvalidStudentError: id is not an integer
																 id is not a positive integer
																 name is empty
																 name is not a string
																 group is not an integer
																 group is not a positive integer
		"""
		errors = []
		# Check if the id is an integer and if it is check if it is positive
		try:
			int(student.getId())
		except ValueError:
			errors.append("id is not an integer")
		else:
			if int(student.getId()) < 0:
				errors.append("id is not a positive integer")
		# Check if the name is a string and if it is check if it is empty
		try:
			int(student.getName())
			assert False
		except AssertionError:
			errors.append("name is not a string")
		except ValueError:
			pass
		if str(student.getName()) == "":
			errors.append("name is empty")
		# Check if the group is an integer and if it is check if it is positive
		try:
			int(student.getGroup())
		except ValueError:
			errors.append("group is not an integer")
		else:
			if int(student.getGroup()) < 0:
				errors.append("group is not a positive integer")
		# Raise an InvalidStudentError if any field is invalid
		if len(errors):
			raise InvalidStudentError(errors)


class ProblemValidator:
	def validateProblem(self, problem):
		"""
		A function that checks if the received instance of the Problem class is valid.
		Preconditions: problem: an instance of the Problem class
		Post-conditions: -
		Raises: InvalidProblemError: id does not follow the required format
																 labNumber or problemNumber is not an integer
																 labNumber or problemNumber is not a positive integer
																 description is empty
																 deadline does not following the required format
																 deadline day is not valid
																 deadline month is not valid
																 deadline year is not valid
		"""
		errors = []
		# Check if the id has the required format and if the labNumber and problemNumber are positive integers
		if len(problem.getId().split("_")) == 2:
			try:
				int(problem.getId().split("_")[0])
				int(problem.getId().split("_")[1])
			except ValueError:
				errors.append("labNumber or problemNumber is not an integer")
			else:
				if int(problem.getId().split("_")[0]) < 0 or int(problem.getId().split("_")[1]) < 0:
					errors.append("labNumber or problemNumber is not a positive integer")
		else:
			errors.append("id does not follow the required format")
		# Check if the description is valid
		if problem.getDescription() == "":
			errors.append("description is empty")
		# Check if the deadline is valid
		if len(problem.getDeadline().split("/")) == 3:
			# Check if the month is valid
			try:
				int(problem.getDeadline().split("/")[0])
			except ValueError:
				errors.append("deadline month is not valid")
			else:
				if not 0 < int(problem.getDeadline().split("/")[0]) <= 12:
					errors.append("deadline month is not valid")
			# Check if the day is valid
			try:
				int(problem.getDeadline().split("/")[1])
			except ValueError:
				errors.append("deadline day is not valid")
			else:
				if not 0 < int(problem.getDeadline().split("/")[1]) <= 31:
					errors.append("deadline day is not valid")
			# Check if the year is valid
			try:
				int(problem.getDeadline().split("/")[2])
			except ValueError:
				errors.append("deadline year is not valid")
			else:
				if not 0 < int(problem.getDeadline().split("/")[2]):
					errors.append("deadline year is not valid")
		else:
			errors.append("deadline does not following the required format")
		# If any field is invalid raise a InvalidProblemError
		if len(errors):
			raise InvalidProblemError(errors)

class AssignmentValidator:
	
	def validateAssignment(self, assignment):
		"""
		A function that checks if the received instance of Assignment class is valid.
		Preconditions: assignment: an instance of the Assignment class.
		Post-conditions: -
		Raises: InvalidAssignmentError: mark is not an integer
																		mark is not an integer between 0 and 10
		"""
		# Check if mark is an integer between 0 and 10
		errors = []
		try:
			int(assignment.getMark())
		except ValueError:
			errors.append("mark is not an integer")
		else:
			if not 0 <= int(assignment.getMark()) <= 10:
				errors.append("mark is not an integer between 0 and 10")
		# If the mark is invalid throw an InvalidAssigmentError
		if len(errors):
			raise InvalidAssignmentError(errors)