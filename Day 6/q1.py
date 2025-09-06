def max_numbers(a, b, c):
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    nmax = max(list) # Built-in Functions
    print(f"Maximum number among three nos. is {nmax}")

a = int(input("Enter a.\n"))
b = int(input("Enter b.\n"))
c = int(input("Enter c.\n"))

max_numbers(a, b, c)