# Program to calculate simple interest

# Input principal amount, time in years, and rate of interest from the user
p = float(input("Enter Principal. "))
t = float(input("Enter Time in Years. "))
r = float(input("Enter Rate Of Interest. "))

# Calculate simple interest using the formula: SI = (P * R * T) / 100
si = (p*r*t)/100

# Display the calculated simple interest
print("Simple Interest is",si)