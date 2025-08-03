MP = int(input("Enter Marked Price: "))

if(MP >10000):
    N_amt = MP - ((MP*20)/100)
elif(MP>=7000 and MP<=10000):
    N_amt = MP - ((MP * 15) / 100)
else:
    N_amt = MP - ((MP * 10) / 100)

print("NET AMOUNT:", N_amt)