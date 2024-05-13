# first = int(input("Enter first number : "))
# second = int(input("Enter second number : "))
# sum = first + second
# print("The sum is",sum)


mylist = [[1,7],[3,7],[1,7],[5,8],[3,7]]
setlist = []
for i in mylist:
    if i not in setlist:
        setlist.append(i)
print(setlist)
