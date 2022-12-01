#syntax
# if condition:
#code # if condition is true then code excetued
age=int(input())
if age>15:
    print("you are eligible")
else:
    print("you are not eligible")
# pass sateement
x=int(input())
if x>18:
    pass
# elif staement
x=int(input())
if x>1 and x<5:
    print("ticket price 100")
elif x==0:
    print("you are eligible")
elif x>5 and x<16:
    print("ticket price 200")
else:
    print("ticket price 500")
