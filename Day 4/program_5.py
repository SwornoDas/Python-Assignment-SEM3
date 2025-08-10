start = int(input("Enter Starting Range.\n"))
end = int(input("Enter Ending Range.\n"))
f = 1
c = 0
print("Prime Numbers from {start} to {end} are-\n")
for i in range(start, end):
    for j in range(1, i + 1):
        if (j % 2 == 0):
            c += 1
            break
    if (c == 2):
        print(i)
        c = 0
