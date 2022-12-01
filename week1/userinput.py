#user input--input function
name=input("type your name: ")
print("hello"+name)
num_one=int(input("first num"))
num_two=int(input("second num"))
print(num_one+num_two)
#two or more input in one line
#name=input('your name')
#age=input('your age')
name,age=input("your name age").split(",")
print(name)
print(age)
