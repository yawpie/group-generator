import os
file = open(os.getcwd()+"\\students.txt","a") # "a" for append

while True:
    name = input("Nama: ")
    studentID = input("NIM: ")
    sex = input("Gender: ")

    file.write("\""+name+"\",")
    file.write("\""+studentID+"\",")
    file.write("\""+sex+"\"\n")
    print()
    isEnd = input("end? (Y/N) ")
    if isEnd == "y" or isEnd == "Y":
        break
    print()