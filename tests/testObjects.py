import unittest
from domain.objects import Student, Problem, Assignment

class TestObjects(unittest.TestCase):
	
	def setUp(self):
		"""
		A function that sets up the data needed for the tests.
		Preconditions: -
		Post-conditions: -
		"""
		# Setup student
		self.studentId = 1
		self.name = "Ionescu"
		self.group = 200
		self.student = Student(self.studentId, self.name, self.group)
		# Setup problem
		self.problemId = "1_1"
		self.description = "A problem."
		self.deadline = "12/20/2022"
		self.problem = Problem(self.problemId, self.description, self.deadline)
		# Set up assignment
		self.mark = 5
		self.assignment = Assignment(self.student, self.problem, self.mark)
		
	
	def testGetters(self):
		"""
		A function that checks if the getters of the objects work properly.
		Raises: AssertionError
		"""
		# Test Student getters
		self.assertEqual(self.studentId, self.student.getId())
		self.assertEqual(self.name, self.student.getName())
		self.assertEqual(self.group, self.student.getGroup())
		# Test Problem getters
		self.assertEqual(self.problemId, self.problem.getId())
		self.assertEqual(self.description, self.problem.getDescription())
		self.assertEqual(self.deadline, self.problem.getDeadline())
		# Test Assignment getters
		self.assertEqual(self.studentId, self.assignment.getStudentId())
		self.assertEqual(self.name, self.assignment.getName())
		self.assertEqual(self.group, self.assignment.getGroup())
		self.assertEqual(self.problemId, self.assignment.getProblemId())
		self.assertEqual(self.description, self.assignment.getDescription())
		self.assertEqual(self.deadline, self.assignment.getDeadline())
		self.assertEqual(self.mark, self.assignment.getMark())
		
	def testSetters(self):
		"""
		A function that checks if the setters of the objects work properly.
		Raises: Assertion Error
		"""
		# Test Student setters
		self.studentId = 2
		self.name = "Andrei"
		self.group = 203
		self.student.setId(self.studentId)
		self.student.setName(self.name)
		self.student.setGroup(self.group)
		self.assertEqual(self.studentId, self.student.getId())
		self.assertEqual(self.name, self.student.getName())
		self.assertEqual(self.group, self.student.getGroup())
		# Test Problem setters
		self.problemId = "2_2"
		self.description = "AAAAA"
		self.deadline = "10/10/2010"
		self.problem.setId(self.problemId)
		self.problem.setDescription(self.description)
		self.problem.setDeadline(self.deadline)
		self.assertEqual(self.problemId, self.problem.getId())
		self.assertEqual(self.description, self.problem.getDescription())
		self.assertEqual(self.deadline, self.problem.getDeadline())
		# Test Assignment setters
		self.mark = 10
		self.assignment.setMark(self.mark)
		self.assertEqual(self.mark, self.assignment.getMark())
		
if __name__ == '__main__':
	unittest.main()