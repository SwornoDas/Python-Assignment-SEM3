# Program to calculate the minimum number of currency notes required for a given amount

# Input the amount in rupees from the user
amt = int(input("Enter Amount - "))

# Calculate number of 500 rupee notes
amt500 = int(amt/500)
print("Rs. 500 =",amt500)
amt = amt - (amt500*500)

# Calculate number of 200 rupee notes
amt200 = int(amt/200)
print("Rs. 200 =",amt200)
amt = amt - (amt200*200)

# Calculate number of 100 rupee notes
amt100 = int(amt/100)
print("Rs. 100 =",amt100)
amt = amt - (amt100*100)

# Calculate number of 50 rupee notes
amt50 = int(amt/50)
print("Rs. 50 =",amt50)
amt = amt - (amt50*50)

# Calculate number of 20 rupee notes
amt20 = int(amt/20)
print("Rs. 20 =",amt20)
amt = amt - (amt20*20)

# Calculate number of 10 rupee notes
amt10 = int(amt/10)
print("Rs. 10 =",amt10)
amt = amt - (amt10*10)

# Calculate number of 2 rupee coins
amt2 = int(amt/2)
print("Rs. 2 =",amt2)
amt = amt - (amt2*2)

# Calculate number of 1 rupee coins
amt1 = int(amt/1)
print("Rs. 1 =",amt1)
amt = amt - (amt1*1)
