# Program to calculate the bill amount for an item given its quantity sold, value, discount and tax

# Input quantity, price per item, discount per item, and tax percentage from the user
QT = int(input("Enter Quantity : "))
VALUE = int(input("Enter Value : "))
DIS = int(input("Enter Discount Percentage : "))
TAX = int(input("Enter Tax : "))

print("**********BILL**********")

# Display quantity and price per item
print("Quantity Sold :",QT)
print("Price Per Item :",VALUE)
print("-----------------")

# Calculate and display total amount before discount
print("Amount :",(QT*VALUE))
# Calculate and display total discount (assuming DIS is discount per item)
print("DISCOUNT : -",(QT*DIS))
print("-----------------")

# Calculate and display discounted total
print("Discounted Total : ",((QT*VALUE)-(QT*DIS)))
# Calculate and display tax (currently hardcoded as 14% instead of using TAX input)
print("Tax :", ((QT*VALUE)-(QT*DIS))*0.14)
# Calculate and display total amount to be paid (discounted total + tax)
print("Total amount to be paid  ", (((QT*VALUE)-(QT*DIS))*0.14)+((QT*VALUE)-(QT*DIS)))
