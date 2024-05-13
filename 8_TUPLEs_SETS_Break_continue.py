# students = ["ram","shyam","krishan","radha","radhika"]

# for student in students:
#     if student == "radha":
#         break
#     print(student)
    
# for student in students:
#     if student == "krishan":
#         continue
#     print(student)


# TUPLS -- same as list, but inmutable(we can't able to perform operation like
#          insert,append,clear,remeove,etc.). We use parentheis () to represent it.

marks = (95,98,97,97,97)
# marks[0]=99    # TypeError: 'tuple' object does not support item assignment
print(len(marks))
print(marks.count(97))
print(marks.index(97))
print(max(marks))

person = "ram","shyam","abhi"   # By default this is Tupls
print(person)


# SETS -- if u want no duplicate element then we define list as sets.
#         To represent a sets we use curly braces {}. Sets are called 
#         unordered list.
marks = {98,95,97,97,97}
# print(marks[0])            # TypeError: 'set' object is not subscriptable
for score in marks:
    print(score)