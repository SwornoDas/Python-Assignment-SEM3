n = int(input("Enter a no. "))
s = 0
k = n
while(k > 0):
    s+= ((k%10)**len(str(n)))
    k//= 10
if s == n:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
