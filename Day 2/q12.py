num = int(input("Enter a 4-digit number: "))

thousands = num // 1000
hundreds = (num % 1000) // 100
tens = (num % 100) // 10
units = num % 10
print("Thousands place:", thousands)
print("Hundreds place:", hundreds)
print("Tens place:", tens)
print("Units place:", units)