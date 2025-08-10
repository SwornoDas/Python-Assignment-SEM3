n = int(input("Enter a no. "))
rev = 0

while(n > 0):
    rev = rev * 10 + (n%10)
    n//= 10
print(f"Reversed Number : {rev}")
