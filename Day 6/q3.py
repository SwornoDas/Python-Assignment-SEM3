def func1(num):
    start = int(input("Enter starting range. "))
    end = int(input("Enter ending range. "))
    for i in range(start,end):
        if i == num:
            print(f"Yes {num} falls in the given range.")
            break
num = int(input("Enter a no.\n"))
func1(num)