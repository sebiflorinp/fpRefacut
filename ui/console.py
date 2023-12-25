from utils.errors import InvalidStudentError, StudentRepoError, InvalidProblemError, ProblemRepoError, \
	InvalidAssignmentError, AssignmentRepoError, AssignmentServiceError
from domain.objects import Student, Problem, Assignment

class Console:
	
	def __init__(self, studentService, problemService, assignmentService):
		"""
		The cosntructor of the Console class.
		Preconditions: studentService: an instance of the StudentService class.
									 problemService: an instance of the ProblemService class.
									 assignmentService: an instance of the AssignmentService class.
		"""
		self.__studentService = studentService
		self.__problemService = problemService
		self.__assignmentService = assignmentService
		
	
	def run(self):
		"""
		The function that starts the application.
		Preconditions: -
		Post-conditions: -
		"""
		# Load data from the files.
		self.__studentService.loadStudents()
		self.__problemService.loadProblems()
		self.__assignmentService.loadAssignments()
		# Print greeting and instructions.
		print("Welcome!!!!")
		print("This application can be used to manage students, laboratory problems and assignments by using the following"
		      " commands:\n  add student\n  add problem\n  delete student\n  delete problem\n  update student\n  "
		      "update problem\n  find student\n  find problem\n  assign problem\n  mark problem\n  display first report\n  "
		      "display second report\n  exit")
		while True:
			# Get a command
			command = input("Enter a command:\n").split(" ")
			# Add feature
			if command[0] == "add":
				# Add a student
				if command[1] == "student":
					# Get needed input
					id = input("Enter id:\n")
					name = input("Enter name:\n")
					group = input("Enter group:\n")
					newStudent = Student(id, name, group)
					# Add student and notify the user if it worked or display the error message.
					try:
						self.__studentService.addStudent(newStudent)
					except InvalidStudentError as message:
						print(message)
					except StudentRepoError as message:
						print(message)
					else:
						self.__studentService.saveStudents()
						print("The student was added successfully.")
				if command[1] == "problem":
					labNumber = input("Enter lab number:\n")
					problemNumber = input("Enter problem number\n")
					description = input("Enter problem description:\n")
					deadline = input("Enter problem deadline:\n")
					problemId = f"{labNumber}_{problemNumber}"
					problem = Problem(problemId, description, deadline)
					try:
						self.__problemService.addProblem(problem)
					except InvalidProblemError as message:
						print(message)
					except ProblemRepoError as message:
						print(message)
					else:
						self.__problemService.saveProblems()
						print("The problem was added successfully.")
			# Delete feature
			if command[0] == "delete":
				if command[1] == "student":
					id = input("Input the id of the student:\n")
					try:
						self.__assignmentService.deleteStudent(id)
					except StudentRepoError as message:
						print(message)
					except AssignmentServiceError as message:
						print(message)
					else:
						self.__studentService.saveStudents()
						self.__assignmentService.saveAssignments()
						print("The student was deleted successfully")
				if command[1] == "problem":
					labNumber = input("Enter the laboratory number:\n")
					problemNumber = input("Enter the problem number:\n")
					id = f"{labNumber}_{problemNumber}"
					try:
						self.__assignmentService.deleteProblem(id)
					except ProblemRepoError as message:
						print(message)
					else:
						self.__problemService.saveProblems()
						self.__assignmentService.saveAssignments()
						print("The problem was deleted successfully.")
			# Find feature
			if command[0] == "find":
				if command[1] == "student":
					id = input("Enter student id:\n")
					try:
						student = self.__studentService.getStudentById(id)
					except StudentRepoError as message:
						print(message)
					else:
						print(student)
				if command[1] == "problem":
					labNumber = input("Enter lab number:\n")
					problemNumber = input("Enter problem number:\n")
					problemId = f"{labNumber}_{problemNumber}"
					try:
						problem = self.__problemService.getProblemById(problemId)
					except ProblemRepoError as message:
						print(message)
					else:
						print(problem)
			# Update Feature
			if command[0] == "update":
				if command[1] == "student":
					id = input("Input the id of the student that will be updated:\n")
					newId = input("Input the new id:\n")
					newName = input("Input the new name:\n")
					newGroup = input("Input the new group:\n")
					newStudent = Student(newId, newName, newGroup)
					try:
						self.__assignmentService.updateStudent(id, newStudent)
					except InvalidStudentError as message:
						print(message)
					except StudentRepoError as message:
						print(message)
					except AssignmentServiceError as message:
						print(message)
					else:
						self.__assignmentService.saveAssignments()
						self.__studentService.saveStudents()
						print("The student was updated successfully.")
				if command[1] == "problem":
					laboratoryNumberToUpdate = input("Enter the laboratory number of the problem that will be updated\n")
					problemNumberToUpdate = input("Enter the problem number of the problem that will be updated\n")
					idToUpdate = f"{laboratoryNumberToUpdate}_{problemNumberToUpdate}"
					updatedLabNumber = input("Enter the updated laboratory number:\n")
					updatedProblemNumber = input("Enter the updated problem number:\n")
					updatedId = f"{updatedLabNumber}_{updatedProblemNumber}"
					updatedDescription = input("Enter the updated description:\n")
					updatedDeadline = input("Enter the updated deadline:\n")
					updatedProblem = Problem(updatedId, updatedDescription, updatedDeadline)
					try:
						self.__assignmentService.updateProblem(idToUpdate, updatedProblem)
					except AssignmentServiceError as message:
						print(message)
					except InvalidProblemError as message:
						print(message)
					except ProblemRepoError as message:
						print(message)
					else:
						self.__assignmentService.saveAssignments()
						self.__problemService.saveProblems()
						print("The problem was updated successfully.")
			# Assign problem
			if command[0] == "assign" and command[1] == "problem":
				studentId = input("Enter the id of the student:\n")
				labNumber = input("Enter lab number:\n")
				problemNumber = input("Enter problem number\n")
				problemId = f"{labNumber}_{problemNumber}"
				try:
					student = self.__studentService.getStudentById(studentId)
				except StudentRepoError as message:
					print(message)
				else:
					try:
						problem = self.__problemService.getProblemById(problemId)
					except ProblemRepoError as message:
						print(message)
					else:
						assignment = Assignment(student, problem)
						try:
							self.__assignmentService.addAssignment(assignment)
						except InvalidAssignmentError as message:
							print(message)
						except AssignmentRepoError as message:
							print(message)
						else:
							self.__assignmentService.saveAssignments()
							print("The assignment was added successfully.")
			# Mark assignment
			if command[0] == "mark" and command[1] == "assignment":
				studentId = input("Enter the id of the student\n")
				labNumber = input("Enter the number of the laboratory\n")
				problemNumber = input("Enter the number of the problem\n")
				mark = input("Enter mark:\n")
				assignmentId = f"{studentId}__{labNumber}_{problemNumber}"
				try:
					self.__assignmentService.markAssignment(assignmentId, mark)
				except AssignmentServiceError as message:
					print(message)
				except AssignmentRepoError as message:
					print(message)
				else:
					self.__assignmentService.saveAssignments()
					print("The assignment was marked successfully.")
			# Reports
			if command[0] == "display":
				if command[1] == "first" and command[2] == "report":
					labNumber = input("Enter the laboratory number:\n")
					problemNumber = input("Enter the problem number:\n")
					problemId = f"{labNumber}_{problemNumber}"
					try:
						results = self.__assignmentService.returnSortedMarks(problemId)
					except AssignmentServiceError as message:
						print(message)
					except AssignmentRepoError as message:
						print(message)
					else:
						for student in results:
							print(f"{student[0]} {student[1]}")
				if command[1] == "second" and command[2] == "report":
					dataToPrint = self.__assignmentService.getStudentsWhoFail()
					if len(dataToPrint) == 0:
						print("All students have passed")
					else:
						for student in dataToPrint:
							print(f"{student[0]}, {student[1]}")
			# Exit
			if command[0] == "exit":
				break
				assignments = self.__assignmentService.getAll()
				for assignment in assignments:
					print(assignment)

