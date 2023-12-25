import unittest
from domain.objects import Student, Problem, Assignment
from repository.repo import StudentRepo, ProblemRepo, AssignmentRepo
from utils.errors import StudentRepoError, ProblemRepoError, AssignmentRepoError

class TestStudentRepo(unittest.TestCase):
	
	def setUp(self):
		"""
		A function that prepares the data needed to run the tests.
		"""
		# Save data to put back in the file
		self.students = []
		with open("files/students.txt", "r") as file:
			data = file.readline().strip().split(", ")
			while len(data) == 3:
				id = int(data[0])
				name = data[1]
				group = int(data[2])
				student = Student(id, name, group)
				self.students.append(student)
				data = file.readline().strip().split(", ")
		# Add some data to the file
		with open("files/students.txt", "w") as file:
			file.write("1, Ionescu, 200\n")
			file.write("2, Georgescu, 201\n")
		# Create some students
		self.id1 = 1
		self.name1 = "Ionescu"
		self.group1 = 200
		self.student1 = Student(self.id1, self.name1, self.group1)
		self.id2 = 2
		self.name2 = "Georgescu"
		self.group2 = 201
		self.student2 = Student(self.id2, self.name2, self.group2)
		# Create repo and add 2 students
		self.repo = StudentRepo()
		self.repo.addStudent(self.student1)
		self.repo.addStudent(self.student2)
		
	def tearDown(self):
		"""
		A function that restores the file to its previous state.
		"""
		with open("files/students.txt", "w") as file:
			for student in self.students:
				file.write(f"{student.getId()}, {student.getName()}, {student.getGroup()}\n")
	
	def testGetAll(self):
		"""
		A function that check if the getAll function works properly.
		Raises: AssertionError
		"""
		# Check if the function returns the two students from the repo properly
		students = self.repo.getAll()
		self.assertEqual(self.student1, students[0])
		self.assertEqual(self.student2, students[1])

	def testGetStudentById(self):
		"""
		A function that checks if the getStudentById function works properly.
		Raises: AssertionError
		"""
		# Check if it returns a certain student properly
		self.assertEqual(self.student2, self.repo.getStudentById(self.id2))
		# Check if it throws a StudentRepoError when trying to get a student using a bad id.
		badId = 21
		self.assertRaises(StudentRepoError, self.repo.getStudentById, badId)

	def testAddStudent(self):
		"""
		A function that checks if the addStudent function works properly.
		Raises: AssertionError
		"""
		newId = 3
		newName = "Avram"
		newGroup = 203
		newStudent = Student(newId, newName, newGroup)
		# Check if the function adds a new student properly.
		self.repo.addStudent(newStudent)
		self.assertEqual(newStudent, self.repo.getAll()[2])
		# Check if the function throws a StudentRepoError when trying to add a student that has the id of another student 
		# in the repo
		self.assertRaises(StudentRepoError, self.repo.addStudent, self.student1)

	def testDeleteStudentById(self):
		"""
		A function that checks if the function deleteStudentById works properly.
		Raises: AssertionError
		"""
		# Check if the function can delete a student properly
		self.repo.deleteStudentById(self.id1)
		self.assertEqual(self.student2, self.repo.getAll()[0])
		# Check if the function throws a StudentRepoError when trying to delete a student using an id that isn't in the repo.
		self.assertRaises(StudentRepoError, self.repo.deleteStudentById, self.id1)
	
	def testUpdateStudentById(self):
		"""
		A function that checks if the function updateStudentById works properly.
		Raises: AssertionError
		"""
		# Check if the function can update a student properly.
		updatedId = 3
		updatedName = "Georgiana"
		updatedGroup = 213
		updatedStudent = Student(updatedId, updatedName, updatedGroup)
		self.repo.updateStudentById(self.id1, updatedStudent)
		# Check index one due to how the update operation works (delete the outdated student and add the new one)
		self.assertEqual(updatedStudent, self.repo.getAll()[1])
		# Check if the function throws a StudentRepoError when trying to update a student using a bad id.
		badId = 200
		self.assertRaises(StudentRepoError, self.repo.updateStudentById, badId, updatedStudent)
		# Check if the function throws a StudentRepoError when update operation leads to the apparition of duplicates.
		self.assertRaises(StudentRepoError, self.repo.updateStudentById, self.id2, updatedStudent)
	
	def testStoreData(self):
		"""
		A function that checks if the function storeData works properly.
		Raises: AssertionError
		"""
		# Write data into file
		self.repo.storeData()
		# Check if the students match
		with open("files/testStudent.txt", "r") as file:
			data = file.readline().strip().split(", ")
			count = 0
			while len(data) == 3:
				id = int(data[0])
				name = data[1]
				group = int(data[2])
				student = Student(id, name, group)
				self.assertEqual(student, self.repo.getAll()[count])
				count += 1
				data = file.readline().strip().split(", ")
	
	def testLoadData(self):
		"""
		A function that checks if the function loadData works properly.
		Raises: AssertionError
		"""
		# Check get data from file
		self.repo.loadData()
		data = self.repo.getAll()
		# Check if the data matches
		self.assertEqual(data[0], self.student1)
		self.assertEqual(data[1], self.student2)

class TestProblemRepo(unittest.TestCase):
	
	def setUp(self):
		"""
		A function that prepares the data needed for the tests.
		"""
		# Save the initial data
		self.problems = []
		with open("files/problems.txt", "r") as file:
			data = file.readline().strip().split(", ")
			while len(data) == 3:
				id = data[0]
				description = data[1]
				deadline = data[2]
				problem = Problem(id, description, deadline)
				self.problems.append(problem)
				data = file.readline().strip().split(", ")
		# Create to problems
		self.id1 = "1_1"
		self.description1 = "AAAAA"
		self.deadline1 = "10/10/2010"
		self.problem1 = Problem(self.id1, self.description1, self.deadline1)
		self.id2 = "1_2"
		self.description2 = "BBBBBBBB"
		self.deadline2 = "1/1/2001"
		self.problem2 = Problem(self.id2, self.description2, self.deadline2)
		# Write those problems in the test file.
		with open("files/testProblem.txt", "w") as file:
			file.write(f"{self.id1}, {self.description1}, {self.deadline1}\n")
			file.write(f"{self.id2}, {self.description2}, {self.deadline2}\n")
		# Add problems in the repo
		self.repo = ProblemRepo()
		self.repo.addProblem(self.problem1)
		self.repo.addProblem(self.problem2)
	
	def tearDown(self):
		"""
		A function that restores the file to its previous state.
		"""
		with open("files/problems.txt", "w") as file:
			for problem in self.problems:
				file.write(f"{problem.getId()}, {problem.getDescription()}, {problem.getDeadline()}\n")
				
	def testGetProblemById(self):
		"""
		A function that checks if the getProblemById function works properly.
		Raises: AssertionError
		"""
		# Check if the function returns a problem properly.
		self.assertEqual(self.problem1, self.repo.getProblemById(self.id1))
		# Check if the function throws a ProblemRepoError when trying to get a problem using a bad id.
		badId = "3_3"
		self.assertRaises(ProblemRepoError, self.repo.getProblemById, badId)
		
	def testGetAll(self):
		"""
		A function that checks if the getAll function works properly.
		Raises: AssertionError
		"""
		# Check if the problems are returned properly.
		problems = self.repo.getAll()
		self.assertEqual(self.problem1, problems[0])
		self.assertEqual(self.problem2, problems[1])
	
	def testAddProblem(self):
		"""
		A function that checks if the addProblem function works properly.
		Raises: AssertionError
		"""
		# Check if the function adds a problem properly.
		newId = "2_2"
		newDescription = "CCCCCC"
		newDeadline = "2/2/2002"
		newProblem = Problem(newId, newDescription, newDeadline)
		self.repo.addProblem(newProblem)
		self.assertEqual(self.repo.getAll()[2], newProblem)
		# Check if the function throws a ProblemRepoError when trying to add a problem with an id that already exists in the repo.
		self.assertRaises(ProblemRepoError, self.repo.addProblem, self.problem1)
	
	def testDeleteProblemById(self):
		"""
		A function that checks if the deleteProblemById works properly.
		Raises: AssertionError
		"""
		# Check if the function can delete a problem properly.
		self.repo.deleteProblemById(self.id1)
		self.assertEqual(self.problem2, self.repo.getAll()[0])
		# Check if the function throws a ProblemRepoError when trying to delete a problem using an id that is not in the repo.
		self.assertRaises(ProblemRepoError, self.repo.deleteProblemById, self.id1)
	
	def testUpdateProblemById(self):
		"""
		A function that checks if the updateProblemById function works properly.
		Raises: AssertionError
		"""
		# Check if the function can update a problem properly.
		updatedId = "3_3"
		updatedDescription = "CCCCCc"
		updatedDeadline = "12/13/2013"
		updatedProblem = Problem(updatedId, updatedDescription, updatedDeadline)
		self.repo.updateProblemById(self.id1, updatedProblem)
		self.assertEqual(self.repo.getProblemById(updatedId), updatedProblem)
		self.assertRaises(ProblemRepoError, self.repo.getProblemById, self.id1)
		# Check if the function throws a ProblemRepoError when trying to update a problem using an id that isn't in the repo
		self.assertRaises(ProblemRepoError, self.repo.updateProblemById, self.id1, self.problem1)
		# Check if the function throws a ProblemRepoError when the update operation creates duplicates in the repo
		self.assertRaises(ProblemRepoError, self.repo.updateProblemById, self.id2, updatedProblem)
	
	def testStoreData(self):
		"""
		A function that checks if the storeData function works properly.
		Raises: AssertionError
		"""
		# Check if the data was stored properly.
		self.repo.storeData()
		with open("files/problems.txt", "r") as file:
			data = file.readline().strip().split(", ")
			count = 0
			while len(data) == 3:
				id = data[0]
				description = data[1]
				deadline = data[2]
				problem = Problem(id, description, deadline)
				self.assertEqual(problem, self.repo.getAll()[count])
				count += 1
				data = file.readline().strip().split(", ")
	
	def testLoadData(self):
		"""
		A function that checks fi the loadData function works properly.
		Raises: AssertionError
		"""
		# Check if the data is loaded properly.
		self.repo.loadData()
		data = self.repo.getAll()
		print(data[0])
		print(self.problem1)
		self.assertEqual(data[0], self.problem1)
		self.assertEqual(data[1], self.problem2)

class TestAssignmentRepo(unittest.TestCase):
	
	def setUp(self):
		"""
		A function that sets up the data needed for the tests.
		"""
		# Save initial data
		self.assignments = []
		with open("files/assignments.txt", "r") as file:
			data = file.readline().strip().split(", ")
			while len(data) == 7:
				studentId = int(data[0])
				name = data[1]
				group = int(data[2])
				problemId = data[3]
				description = data[4]
				deadline = data[5]
				mark = data[6]
				student = Student(studentId, name, group)
				problem = Problem(problemId, description, deadline)
				assignment = Assignment(student, problem, mark)
				self.assignments.append(assignment)
				data = file.readline().strip().split(", ")
		# Create two assignments
		self.idStudent1 = 1
		self.name1 = "Ionescu"
		self.group1 = 200
		self.student1 = Student(self.idStudent1, self.name1, self.group1)
		self.idProblem1 = "1_1"
		self.description1 = "AAAAA"
		self.deadline1 = "10/10/2010"
		self.problem1 = Problem(self.idProblem1, self.description1, self.deadline1)
		self.mark1 = 8
		self.assignment1 = Assignment(self.student1, self.problem1, self.mark1)
		self.idStudent2 = 2
		self.name2 = "Georgescu"
		self.group2 = 201
		self.student2 = Student(self.idStudent2, self.name2, self.group2)
		self.idProblem2 = "1_2"
		self.description2 = "BBBBBBBB"
		self.deadline2 = "1/1/2001"
		self.problem2 = Problem(self.idProblem2, self.description2, self.deadline2)
		self.mark2 = 6
		self.assignment2 = Assignment(self.student2, self.problem2, self.mark2)
		# Add those assignments in a file
		with open("files/testAssignment.txt", "w") as file:
			file.write(f"{self.idStudent1}, {self.name1}, {self.group1}, {self.idProblem1}, {self.description1}, {self.deadline1}, {self.mark1}\n")
			file.write(f"{self.idStudent2}, {self.name2}, {self.group2}, {self.idProblem2}, {self.description2}, {self.deadline2}, {self.mark2}\n")
		# Add those assignments to the repo
		self.repo = AssignmentRepo()
		self.repo.addAssignment(self.assignment1)
		self.repo.addAssignment(self.assignment2)
		
	def tearDown(self):
		"""
		A function that restores the file to the state it was before the test.
		"""
		with open("files/assignments.txt", "w") as file:
			for assignment in self.assignments:
				file.write(f"{assignment.getStudentId()}, {assignment.getName()}, {assignment.getGroup()}, {assignment.getProblemId()}, {assignment.getDescription()}, {assignment.getDeadline()}, {assignment.getMark()}\n")
	
	def testGetAllAssignments(self):
		"""
		A function that checks if the getAllAssignments function works properly.
		Raises: Assertion Error
		"""
		assignments = self.repo.getAll()
		self.assertEqual(self.assignment1, assignments[0])
		self.assertEqual(self.assignment2, assignments[1])

	def testAddAssignment(self):
		"""
		A function that check if the addAssignment function works properly.
		Raises: AssertionError
		"""
		# Create new assignment
		assignment3 = Assignment(self.student1, self.problem2)
		# Add assignment3 to the repo
		self.repo.addAssignment(assignment3)
		self.assertEqual(assignment3, self.repo.getAll()[2])
		# Check if the function throws an AssignmentRepoError when there's already another assignment with the same id.
		self.assertRaises(AssignmentRepoError, self.repo.addAssignment, self.assignment1)
	
	def testStoreData(self):
		"""
		A function that checks if the storeData function works properly.
		Raises: AssertionError
		"""
		self.repo.storeData()
		# Check if the data was stored properly.
		with open("files/assignments.txt", "r") as file:
			data = file.readline().strip().split(", ")
			count = 0
			while len(data) == 7:
				studentId = int(data[0])
				name = data[1]
				group = int(data[2])
				problemId = data[3]
				description = data[4]
				deadline = data[5]
				mark = data[6]
				student = Student(studentId, name, group)
				problem = Problem(problemId, description, deadline)
				assignment = Assignment(student, problem, mark)
				self.assertEqual(assignment, self.repo.getAll()[count])
				count += 1
				data = file.readline().strip().split(", ")
	
	def testLoadData(self):
		"""
		A function that checks if the loadData function works properly.
		Raises: AssertionError
		"""
		self.repo.loadData()
		assignments = self.repo.getAll()
		self.assertEqual(self.assignment1, assignments[0])
		self.assertEqual(self.assignment2, assignments[1])