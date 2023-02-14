import unittest

from Student import Student, Assignment, Event

class TestAssignment(unittest.TestCase):
    def test_getPercentage(self):
        assignment = Assignment('Assignment 1', 80, 100, 'Homework')
        self.assertEqual(assignment.getPercentage(), 80/100)

        assignment = Assignment('Assignment 2', 100, 100, 'Homework')
        self.assertEqual(assignment.getPercentage(), 100/100)

        assignment = Assignment('Assignment 3', 86, 100, 'Homework')
        self.assertEqual(assignment.getPercentage(), 86/100)

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student('Brec Buster', '11019h', 'Brecey', 2002)
        self.student.assignments = [
            Assignment('Assignment 1', 80, 100, 'Homework'),
            Assignment('Assignment 2', 100, 100, 'Homework'),
            Assignment('Assignment 3', 86, 100, 'Homework'),
            Assignment('Exam 1', 281, 300, 'Exam'),
            Assignment('Assignment 4', 93, 100, 'Homework'),
            Assignment('Assignment 5', 93, 100, 'Homework'),
            Assignment('Assignment 6', 97, 100, 'Homework'),
            Assignment('Exam 2', 279, 300, 'Exam'),
        ]
        self.student.events = [
            Event('Lecture 1', 'lecture', 0),
            Event('Lecture 2', 'lecture', 0),
            Event('Meeting 1', 'meeting', 0),
            Event('Pot Luck', 'party', 15),
            Event('Lecture 3', 'lecture', 0),
            Event('Lecture 4', 'lecture', 0),
            Event('Meeting 2', 'meeting', 0),
            Event('Lecture 5', 'lecture', 0),
            Event('Lecture 6', 'lecture', 0),
        ]

    def test_addEvent(self):
        self.student.addEvent(Event('Workshop', 'workshop', 20))
        self.assertEqual(len(self.student.events), 10)

    def test_countMeetings(self):
        self.assertEqual(self.student.countMeetings(), 2)

    def test_getGrade(self):
        self.assertAlmostEqual(self.student.getGrade(), 0.9241666666666667)

    def test_getLetterGrade(self):
        self.assertEqual(self.student.getLetterGrade(), 'A')

if __name__ == '__main__':
    unittest.main()
