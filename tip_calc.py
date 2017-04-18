#tip_calc
amount = float(input("Total bill amount?"))
service = input("Level of service? (good, fair, bad)")
if service == "bad":
    tip = (amount * 10) / 100.0
elif service == "fair":
    tip = (amount * 15) / 100.0
elif service == "good":
    tip = (amount * 20) / 100.0
total = amount + tip

print("Tip amount: $" + "{:.2f}" .format(tip))
print("Total amount: $" + "{:.2f}" .format(total))
