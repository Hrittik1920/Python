# mylist = []
# rows = int(input("Enter rows: "))
# cols = int(input("Enter cols: "))
# for i in range(rows):
#     a=[]
#     for j in range(cols):
#         a.append(int(input()))
#     mylist.append(a)
# print(mylist)
# for i in range(rows):
#     for j in range(cols):
#         print(mylist[i][j] , end=" ")
#     print()


# myTuple = ([4,5,6,7,8,5,7,8],(4,5,6,4,3),"maths",5)
# myTuple[0].append("hard")
# print(myTuple[0])
# print(myTuple[3])


# lis = [4,5,6,7,3,3,6,7,4]
# lis.sort(reverse=True)
# print(lis)
# lis = tuple(lis)
# print(lis)
# lis = set(lis)
# lis = list(lis)
# print(lis) 
# for i in lis:
#     print(i,end=" ")



# mylist = [[1,4],[4,5],[3,4],[1,4],[6,9]]
# mylist = list(set(map(tuple,mylist)))
# print(mylist)

lis = {3,4,5,6,7,5,8}
lis[7]=6
print(lis[7])




# t=int(input())
# for i in range(t):
#     li=[]
#     n=int(input())
#     for j in range(n):
#         k=input()
#         for j in k:
#             li.append(j)
#     a1=0
#     a2=0
#     a3=0
#     a4=0
#     a5=0
#     a6=0
#     a7=0
#     a8=0
#     for t in range(len(li)):
#             if li[t] == 'r':
#                 a1=a1+1
#             elif li[t] == 'a':
#                 a2=a2+1
#             elif li[t] == 't':
#                 a3 = a3+1
#             elif li[t] == 'o':
#                 a4=a4+1
#             elif li[t] == 'u':
#                 a8=a8+1
#             elif li[t] == 'i':
#                 a5=a5+1
#             elif li[t] == 'l':
#                 a6=a6+1
#             elif li[t] == 'e':
#                 a7=a7+1
#     if a1>=1 and a2>=2 and a3>=2 and a5>=1 and a8>=1 and c_i>=1 and a6>=2 and a7>=1:
#         print(1)
#     else:
#         print(0)
