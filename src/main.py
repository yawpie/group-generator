import os
path = os.getcwd()

# ! DO NOT FORGET TO PUT \\ IN FILENAME DURING OBJECT INITIALIZATION


class Student:
    def addName(self, name):
        self.name = name

    def addStudentID(self, studentID):
        self.studentID = studentID

    def addGender(self, gender):
        self.gender = gender


class Line:
    def __init__(self, data="string"):
        self.rawData = data
        firstComma = self.rawData.find(",")
        secondComma = self.rawData.find(",", firstComma + 1)

        # mencari nama sampai menemukan koma pertama
        firstQuote = self.rawData.find("\"", 0, firstComma)
        secondQuote = self.rawData.find("\"", firstQuote+1, firstComma)
        self.firstData = self.rawData[firstQuote+1:secondQuote]

        # mencari NIM sampai menemukan koma kedua
        firstQuote = self.rawData.find("\"", firstComma)
        secondQuote = self.rawData.find("\"", firstQuote+1, secondComma)
        self.secondData = self.rawData[firstQuote+1:secondQuote]

        # mencari Jenis kelamin dengan menggunakan koma kedua sebagai titik awal find()
        firstQuote = self.rawData.find("\"", secondComma)
        secondQuote = self.rawData.find("\"", firstQuote+1)
        self.thirdData = self.rawData[firstQuote+1:secondQuote]

    def printData(self):  # used for debugging
        print("Nama:", self.firstData, "\nNIM:",
              self.secondData, "\nGender:", self.thirdData)


class StudentList:
    nameList = []
    studentIDList = []
    gendersList = []

    def __init__(self, fileName="\\*.txt"):
        file = open(path+fileName, "r")
        rawListData = file.readlines()
        for lines in rawListData:
            lineObj = Line(lines)
            self.nameList.append(lineObj.firstData)
            self.studentIDList.append(lineObj.secondData)
            self.gendersList.append(lineObj.thirdData)


studentlist = StudentList("\\students.txt")
for char in studentlist.nameList:
    print(char)
