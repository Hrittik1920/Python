name = "tony Stark" 

print(name.upper())
print(name.lower())

print(name.find('stark'))

print(name.replace("Stark","Ironman"))
print(name.replace("T","M"))

print("Stark" in name)

print(name.capitalize())

txt1 = "My name is {fname}, I'm {age}"
print(txt1.format(fname = "hrittk",age = "22"))

txt2 = "My name is {0}, I'm {1}"
print(txt2.format("Hrittik",22))

myTuple = ("ram","shyam","sita")
x = "@".join(myTuple)
print(x)

txt = "     banana     "
x = txt.strip()
print("of all fruit",x,"is my favorite")


print(format(14,'b'))



