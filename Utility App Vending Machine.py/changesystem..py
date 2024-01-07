maidubaistock = 5
fijistock = 5

amountdue = 0.00

def changesystem():
    global amountdue
    
    amountinserted = float(input("Please insert amount due: "))
    amountdue = amountdue - amountinserted
    if amountdue != 0:
        changesystem()
    elif amountdue == 0:
        print("Item now being dispensed.")





amount_due = 1.00
amount_inserted = float(input("Please insert amount due: "))
if amount_inserted > 1.00:
    change = amount_inserted - 1.00
    print(f"Your change of ", + change, " now being dispensed")
elif amount_inserted < 1.00:
    while amount_inserted < 1.00:
        amount_inserted = amount_inserted + float(input("Please insert amount due: "))
    