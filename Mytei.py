# def isPrime(a) :
#     if(n == 0 or n == 1) :
#         return False 
#     for i in range(2,int(a**(1/2))):
#         if(a%i == 0) :
#             return False
#     return True

# n = int(input("Enter the number:"))
# storage = []
# for i in range(0,n) :
#     if(isPrime(i)) :
#         storage.append(i)
# print("Prime number between 0 and " + str(n) + " are:")
# print(storage)


##➣ Prime number of 1st 100000 numbers in best time
# import time
# def findPrime(n):
#     prime = [True for i in range(n+1)]
#     p = 2
#     while(p * p <= n):
#         if (prime[p] == True):
#             for i in range(p * p, n + 1, p):
#                 prime[i] = False
#         p += 1
#     c = 0
#     for p in range(2, n):
#         if prime[p]:
#             c += 1
#     return c

# t0 = time.time()
# c = findPrime(100000)
# print("Total prime numbers in range:", c)
# t1 = time.time()
# print("Time required:", t1 - t0)


# #➣ Kaprekar Number
# number = 9
# sum = 0
# temp = number*number
# while temp>0:
#     sum += temp%10
#     temp = temp//10
# if sum == number:
#     print(f"{number} is a Kaprekar number")
# else:
#     print(f"{number} is not a Kaprekar number")


# #➣ Find the highest marks in a single semester and highest marks overall.
# def highest(kwargs: dict): #-> (str, str, int):
#     high = 0
#     marks = ""
#     sem = ""
#     for key, value in kwargs.items():
#         TempMarks, TempValue = highest_sem(value, key)
#         if TempValue>high:
#             high = TempValue
#             marks = TempMarks
#             sem = key
#     return (sem, marks, high)

# def highest_sem(kwargs: dict, args: str): #-> (str, int):
#     high = 0
#     marks = ""
#     for key, value in kwargs.items():
#         if value>high:
#             high = value
#             marks = key
#     return (marks, high)

# marks = {
#     "sem1": {
#         "DSA": 10,
#         "CO": 11,
#         "IT": 10,
#         "MATHS": 4
#     },
#     "sem2": {
#         "DSA": 20,
#         "CO": 21,
#         "IT": 20,
#         "MATHS": 10
#     },
#     "sem3": {
#         "DSA": 15,
#         "CO": 17,
#         "IT": 16,
#         "MATHS": 20
#     }
# }
# sem, sub, marks = highest(marks)
# print(f"Highest marks obtained in {sub} during {sem} is {marks}")


# #➣ Print the total number of vowels and consonants in a string#
# name = "Hrittik"
# vowels = [each for each in name if each in "aeiouAEIOU"]
# print('Number of vowels:', len(vowels), vowels)
# consonants = [each for each in name if each not in "aeiouAEIOU"]
# print('Number of consonants:', len(consonants), consonants)


# #➣ Put double quote to all the strings of a array.
# country = ['Ind', 'Pak', 'Sim','UK']
# double_country = [f'"{ele}"' for ele in country]
# print(double_country)


# # ➣ Create a custom error and raise the error in a factorial program.
# class FactorialError(Exception):
#     def __init__(self, message: str):
#         self.message = message
#         super().__init__(self.message)
# def factorial(x) -> int:
#     if x < 0:
#         raise FactorialError("Sorry, no numbers below zero")
#     if type(x) in [dict, float, str, list, tuple, set, bool]:
#         raise FactorialError("Only int is valid")
#     prod = 1
#     for i in range(1, x+1):
#         prod *= i
#     return prod

# n = -1
# try:
#     fact = factorial(n)
#     print(fact)
# except FactorialError as err:
#     print(err)



# #➣ Use pandas to find bmi of a certain animal from a sample dataset.
# import pandas
# from seaborn import load_dataset
# df = load_dataset('penguins')
# df['bill_length_cm'] = [ i/100 for i in df['bill_length_mm'] ]
# df['bill_depth_cm'] = [ i/100 for i in df['bill_depth_mm'] ]
# df['flipper_length_cm'] = [ i/100 for i in
# df['flipper_length_mm'] ]
# df['bmi'] = [
# (df['body_mass_g'][i]/1000)/(df['bill_depth_cm'][i]*df['bill_depth_cm'][i]) for i in range(len(df['bill_depth_cm']))]
# print(df.head())




# ➣ Take the input of name of object and it method and show the help of the function closely related to the imputed method name.
obj = input("Enter the name of the object to search from = ")
totalMethods = dir(eval(obj))
function = input("Enter function name = ")
j = 0
for method in totalMethods:
    if method.find(function) == -1:
        continue
    print(help(eval(f'{obj}.{method}')))
    j += 1
if not j:
    print("No method found")




