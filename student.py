#!/usr/bin/env python3
# Author ID: pkaur515

class Student:

    # Define the name and student ID number (which is a string) when a student object is created
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    # Display student name and number
    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and display it
    def displayGPA(self):
        gpa = 0.0
        for course in self.courses.keys():
            gpa += self.courses[course]
        if len(self.courses) > 0:
            print('GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses)))
        else:
            print('GPA of student ' + self.name + ' is 0.0')

if __name__ == '__main__':
    # Testing the class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    student1.displayStudent()
    student1.displayGPA()

    student2.displayStudent()
    student2.displayGPA()
