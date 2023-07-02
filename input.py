import os

while True:
    name = input("Nama: ")
    studentID = input("NIM: ")
    sex = input("Gender: ")

    file = open(os.getcwd()+"\\students.txt","a") # "a" for append
    file.write("\""+name+"\",")
    file.write("\""+studentID+"\",")
    file.write("\""+sex+"\"\n")
    print()
    file.close()