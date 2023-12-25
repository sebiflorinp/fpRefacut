from domain.validators import StudentValidator, ProblemValidator, AssignmentValidator
from repository.repo import StudentRepo, ProblemRepo, AssignmentRepo
from business.studentService import StudentService
from business.assignmentService import AssignmentService
from business.labProblemService import ProblemService
from ui.console import Console

#Create Student, Problem and Assignment Services.
studentRepo = StudentRepo()
studentValidator = StudentValidator()
studentService = StudentService(studentRepo, studentValidator)
problemRepo = ProblemRepo()
problemValidator = ProblemValidator()
problemService = ProblemService(problemRepo, problemValidator)
assignmentRepo = AssignmentRepo()
assignmentValidator = AssignmentValidator()
assignmentService = AssignmentService(assignmentRepo, assignmentValidator, studentRepo, problemRepo, studentValidator, problemValidator)

#Create Console.
console = Console(studentService, problemService, assignmentService)

#Run program.
console.run()
