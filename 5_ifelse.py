# age = 2

# if age>=18:
#     print("U r an adult")
#     print("U can vote")
# elif age <18 and age >3:
#     print("you are in school")
# else:
#     print("you are a child")

first = int(input("enter first number : "))
operator = input("enter operator (+,-,*,/,%,**) : ")
second = int(input("enter second number : "))

if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
elif operator == '**':
    print(first ** second)
else:
    print("Invalid operator!")
