age = int(input("Enter Your Age. "))

if(age>=0 and age<12):
    print("Child")
elif age>13 and age<19:
    print("Teen")
elif(age>=20 and age<64):
    print("Adult")
else:
    print("Senior")