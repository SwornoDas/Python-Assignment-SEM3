n = int(input("Enter a no. "))
s = 0
for i in range(1, (n//2)+1):
    s += i
if(s==n):
    print("Perfect Number")
else:
    print("Not a Perfect Number")