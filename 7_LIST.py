# Primitive data type -- str(),int(),float(),bool()
# Complex data type -- List(collection of primitive data types)

# marks = [94,98,87,"maths"]
# print(marks)
# print(marks[-1])

marks = [94,94,98,87,]

print(marks.count(94))
print(marks.index(87))
print(marks.index(94))

marks.append(99)
marks.insert(0,34)

print(marks)
# print(99 in marks)
print(len(marks))

# for score in marks:
#     print(score)

# i=0
# while i<len(marks):
#     print(marks[i])
#     i = i + 1

marks.sort(reverse=True)
print(marks) 

marks.clear()
print(marks)

marks2 = [34,5,89]
marks.append(45)
marks.extend(marks2)
marks.remove(5)
run = marks.copy()
element = marks.pop(1)
marks.__add__(marks2)
print(marks)
print(run)
print(element)
print(marks2)



