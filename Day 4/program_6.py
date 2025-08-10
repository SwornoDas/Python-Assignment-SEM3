num = int(input("Enter a no.\n"))
rev = 0
k = num
while(num > 0):
    r = num%10
    rev = rev*10+r
    num//= 10

if(rev == k):
    print(f"Reversed Number is {rev}")
