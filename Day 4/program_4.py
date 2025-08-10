n = int(input("Enter a range.\n"))
a = 0
b = 1
print(f"First {n} Fibonacci Sequence :\n")
for i in range(1,n+1):
    print(a,"\t")
    c = a+b
    a = b
    b = c