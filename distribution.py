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
# for student in students:
#     print(student, students[student])
    
print()
# print(students.keys())
list1 = list(students.keys())
# print(type(list1))

list2 = list1[:]
shuffle(list2)
diff = conflicting_lists(list1, list2)
while diff:
    shuffle(list2)
    diff = conflicting_lists(list1, list2)
# print(type(list2))

list3 = list1[:]
shuffle(list3)
diff = conflicting_lists(list1, list3) or conflicting_lists(list2, list3)
while diff:
    shuffle(list3)
    diff = conflicting_lists(list1, list3) or conflicting_lists(list2, list3)
# print(type(list3))

list4 = list1[:]
shuffle(list4)
diff = conflicting_lists(list1, list4) or conflicting_lists(list2, list4) or conflicting_lists(list3, list4)
while diff:
    shuffle(list4)
    diff = conflicting_lists(list1, list4) or conflicting_lists(list2, list4) or conflicting_lists(list3, list4)
# print(type(list4))

# dist_list = [list1, list2, list3, list4]
print()
print("Distribuição da Avaliação")
print()
print(len(list1))
print("Lista 1:", list1)
print()
print(len(list2))
print("Lista 2:", list2)
print()
print(len(list3))
print("Lista 3:", list3)
print()
print(len(list4))
print("Lista 4:", list4)

for i in range(len(list1)):
    print("%s\n\t%s\n\t%s\n\t%s\n\n"%(students[list1[i]], students[list2[i]], students[list3[i]], students[list4[i]]))