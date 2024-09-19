# bill and tip calculator
tip = int(input("how much tip do you want to leave, 15%, 18% or 20%: "))
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
myBill_plus_tip = myBill * (1 + tip / 100)
answer = round(myBill_plus_tip / numberOfPeople, 2)
print("You all owe", answer)
