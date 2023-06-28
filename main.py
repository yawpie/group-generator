import os
path = os.getcwd().replace("\\", "/")
path += "/Group Generator"


class Student:
    def addName(self, name):
        self.name = name

    def addStudentID(self, studentID):
        self.studentID = studentID

    def addGender(self, gender):
        self.gender = gender


class StudentList:
    studentListObj = []

    def saveToList(self, inputData, inputList=[]):
        newList = inputList
        newList.append(inputData)
        return newList

    def startReading(self, data):  # taking name and return it to a variable
        changingVariable = ""
        i = 0
        for char in data:
            if (char == "\""):
                if (i == 2):
                    return changingVariable
                i += 1
                continue
            changingVariable += char

    def __init__(self, filePath):  # todo change dir
        self.openFile = open(path + filePath, "r")
        rawData = self.openFile.readlines()
        lineNumber = 1
        for char in rawData:
            if (char == "\n"):
                print("line38")
                lineNumber += 1
        i = 0
        while (i < lineNumber):
            print("line42")
            newStudent = Student()
            newStudent.addName(self.startReading(rawData))
            self.studentListObj = self.saveToList(
                newStudent.name, self.studentListObj)
            i += 1


studentMainList = StudentList("")
for i in range(0, 3):
    print(studentMainList.studentListObj[i])
