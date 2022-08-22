# 🚨 Don't change the code below 👇
from functools import total_ordering


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
#Sem usar SUM e LEN, fazer um loop que some todos os itens da lista e fazer uma média deles 
#Write your code below this row 👇

#soma todas as alturas
total_height = 0
for height in student_heights:
    total_height += height
print (total_height)

#soma o número de itens
number_of_students = 0
for students in student_heights:
    number_of_students += 1
print(number_of_students)

average = total_height / number_of_students

print(round(average))