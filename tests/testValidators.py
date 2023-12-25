import unittest
from domain.objects import Student, Problem, Assignment
from domain.validators import StudentValidator, ProblemValidator, AssignmentValidator
from utils.errors import InvalidStudentError, InvalidProblemError, InvalidAssignmentError

class TestValidator(unittest.TestCase):
	
	def setUp(self):
		"""
		A function that prepares the data required for the tests.
		"""
		# Create students
		self.validStudentId = 1
		self.validName = "Ion"
		self.validGroup = 241
		self.invalidStudentId = "fdsf"
		self.invalidName1 = 24
		self.invalidName2 =  ""
		self.invalidGroup = "fdsfd"
		self.validStudent = Student(self.validStudentId, self.validName, self.validGroup)
		self.invalidStudent1 = Student(self.invalidStudentId, self.validName, self.validGroup)
		self.invalidStudent2 = Student(self.validStudentId, self.invalidName1, self.validGroup)
		self.invalidStudent3 = Student(self.validStudentId, self.invalidName2, self.validGroup)
		self.invalidStudent4 = Student(self.validStudentId, self.validName, self.invalidGroup)
		# Create problems
		self.validProblemId = "1_1"
		self.validDescription = "asddsfdsf"
		self.validDeadline = "10/10/2010"
		self.invalidProblemId1 = "2"
		self.invalidProblemId2 = "fd_2"
		self.invalidProblemId3 = ""
		self.invalidDescription = ""
		self.invalidDeadline1 = "fdsfds"
		self.invalidDeadline2 = "2.2.34"
		self.invalidDeadline3 = "20/20/2000"
		self.invalidDeadline4 = "10/34/2000"
		self.invalidDeadline5 = "10/20/-2000"
		self.validProblem = Problem(self.validProblemId, self.validDescription, self.validDeadline)
		self.invalidProblem1 = Problem(self.invalidProblemId1, self.validDescription, self.validDeadline)
		self.invalidProblem2 = Problem(self.invalidProblemId2, self.validDescription, self.validDeadline)
		self.invalidProblem3 = Problem(self.invalidProblemId3, self.validDescription, self.validDeadline)
		self.invalidProblem4 = Problem(self.validProblemId, self.invalidDescription, self.validDeadline)
		self.invalidProblem5 = Problem(self.validProblemId, self.validDescription, self.invalidDeadline1)
		self.invalidProblem6 = Problem(self.validProblemId, self.validDescription, self.invalidDeadline2)
		self.invalidProblem7 = Problem(self.validProblemId, self.validDescription, self.invalidDeadline3)
		self.invalidProblem8 = Problem(self.validProblemId, self.validDescription, self.invalidDeadline4)
		self.invalidProblem9 = Problem(self.validProblemId, self.validDescription, self.invalidDeadline5)
		# Create assignments
		self.validMark = 4
		self.invalidMark1 = -4
		self.invalidMark2 = "fdfd"
		self.validAssignment = Assignment(self.validStudent, self.validProblem, self.validMark)
		self.invalidAssignment1 = Assignment(self.validStudent, self.validProblem, self.invalidMark1)
		self.invalidAssignment2 = Assignment(self.validStudent, self.validProblem, self.invalidMark2)
		# Create validators
		self.studentValidator = StudentValidator()
		self.problemValidator = ProblemValidator()
		self.assignmentValidator = AssignmentValidator()
	
	def testStudentValidator(self):
		"""
		A function that checks if the StudentValidator works properly.
		Raises: AssertionError
		"""
		# Test if the function doesn't throw an error when it validates a valid student.
		try:
			self.studentValidator.validateStudent(self.validStudent)
		except InvalidStudentError:
			assert False
		# Test if the function throws an error when it validates an invalid student.
		self.assertRaises(InvalidStudentError, self.studentValidator.validateStudent, self.invalidStudent1)
		self.assertRaises(InvalidStudentError, self.studentValidator.validateStudent, self.invalidStudent2)
		self.assertRaises(InvalidStudentError, self.studentValidator.validateStudent, self.invalidStudent3)
		self.assertRaises(InvalidStudentError, self.studentValidator.validateStudent, self.invalidStudent4)
	
	def testProblemValidator(self):
		"""
		A function that checks if the ProblemValidator works properly.
		Raises: AssertionError
		"""
		# Test if the function doesn't throw an error when it validates a valid problem.
		try:
			self.problemValidator.validateProblem(self.validProblem)
		except InvalidProblemError:
			assert False
		# Test if the function throws an error when it validates an invalid problem.
		self.assertRaises(InvalidProblemError, self.problemValidator.validateProblem, self.invalidProblem1)
		self.assertRaises(InvalidProblemError, self.problemValidator.validateProblem, self.invalidProblem2)
		self.assertRaises(InvalidProblemError, self.problemValidator.validateProblem, self.invalidProblem3)
		self.assertRaises(InvalidProblemError, self.problemValidator.validateProblem, self.invalidProblem4)
		self.assertRaises(InvalidProblemError, self.problemValidator.validateProblem, self.invalidProblem5)
		self.assertRaises(InvalidProblemError, self.problemValidator.validateProblem, self.invalidProblem6)
		self.assertRaises(InvalidProblemError, self.problemValidator.validateProblem, self.invalidProblem7)
		self.assertRaises(InvalidProblemError, self.problemValidator.validateProblem, self.invalidProblem8)
		self.assertRaises(InvalidProblemError, self.problemValidator.validateProblem, self.invalidProblem9)		
	
	def testAssignmentValidator(self):
		"""
		A function that checks if the AssignmentValidator works properly.
		Raises: AssertionError
		"""
		# Test if the function doesn't throw an error when it validates a valid assignment.
		try:
			self.assignmentValidator.validateAssignment(self.validAssignment)
		except InvalidAssignmentError:
			assert False
		# Test if the function throws an error when it validates an invalid assignment.
		self.assertRaises(InvalidAssignmentError, self.assignmentValidator.validateAssignment, self.invalidAssignment1)
		self.assertRaises(InvalidAssignmentError, self.assignmentValidator.validateAssignment, self.invalidAssignment2)

if __name__ == '__main__':
    unittest.main()