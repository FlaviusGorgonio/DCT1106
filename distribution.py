import PyPDF2
import csv
from random import shuffle

def conflicting_lists(l1, l2):
    tam = len(l1)
    for i in range(tam):
        if l1[i] == l2[i]:
            return True
    return False


pdfFileObj = open("listapresenca_DCT1106_2022.2_01.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numPages = pdfReader.numPages

print("Páginas:",numPages)

pageObj = pdfReader.getPage(0)
text = pageObj.extractText()

start = text.find("ASSINATURA") + len("ASSINATURA")
print("Posição:", start)

end = text.rfind("Página")
print("Posição:", end)

text = text[start:end]

print()
# print(text)
print()
student_list = text.split('\n')

while '' in student_list:
    student_list.remove('')

student_pos = 1
students = {}
for student in student_list:
    space_pos = student.rfind(' ')
    student = student.removesuffix(str(student_pos))
    student_number = student[space_pos+1:]
    student_name = student[0:space_pos]
    students[student_number] = student_name
    student_pos += 1

print('Foram importados %d alunos'%len(students))
for student in students:
    print(student, students[student])
    