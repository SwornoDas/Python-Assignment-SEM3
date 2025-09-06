def prime(num):
    if num <= 1:
        print(f"{num} is not a Prime Number")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a Prime Number")
            return

    print(f"{num} is a Prime Number")


num = int(input("Enter a number: "))
prime(num)