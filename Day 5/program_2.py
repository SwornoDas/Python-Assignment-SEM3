n = int(input("Enter a no. "))
s = 0
while(n > 0):
    s += (n%10)
    n//= 10
print(f"Sum of digits: {s}")
