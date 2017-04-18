amount = float(input("Total bill amount?"))
service = input("Level of service? (good, fair, bad)")
people = int(input("Split how many ways?"))
if service == "bad":
    tip = (amount * 10) / 100.0
elif service == "fair":
    tip = (amount * 15) / 100.0
elif service == "good":
    tip = (amount * 20) / 100.0
total = amount + tip
split = total / people

print("Tip amount: $" + "{:.2f}" .format(tip))
print("Total amount: $" + "{:.2f}" .format(total))
print("Amount per person: " + "{:.2f}".format(split))
