completemenu = {"Mai Dubai         AED 1.00":  "101",
                "Fiji              AED 8.55":  "102",
                "Al Ain            AED 1.00":  "103",
                "Coca-Cola         AED 3.50":  "104",
                "Pepsi             AED 3.50":  "105",
                "Mountain Dew      AED 3.50":  "106",
                "7Up               AED 3.50":  "107",
                "Coke Zero         AED 5.00":  "108",
                "Diet Pepsi        AED 5.00":  "109",
                "Gatorade          AED 5.00":  "110",
                "Monster Energy    AED 1.00":  "111",
                "Celcius Live Fit  AED 8.00":  "112",
                "Red Bull Zero     AED 9.60":  "113",
                "M&M               AED 3.80":  "201",
                "M&M Peanuts       AED 4.00":  "202",
                "Reese's Pieces    AED 3.30":  "203",
                "KitKat 4 Finger   AED 2.70":  "204",
                "Skittles          AED 2.75":  "205",
                "Snickers          AED 3.15":  "206",
                "Hersheys C&Cream  AED 3.80":  "207",
                "Nestles Milky Bar AED 1.30":  "208"}

maidubaistock = 5
fijistock = 5

amount_inserted = 0.00

threedigit = input("Please Enter the 3-Digit Number of Your Chosen Product: ")
def checkthreedigit():
    global threedigit
    global amount_inserted

    global maidubaistock

    if threedigit == "101":
        if maidubaistock > 0:
            maidubaistock += -1
            amount_inserted = amount_inserted + 1.00

        elif maidubaistock == 0:
            print("Sorry this item is out of stock.")
            threedigit = input("Please Enter the 3-Digit Number of Your Chosen Product:")
            checkthreedigit()

    elif threedigit == "102":
        if fijistock != 0:
            fijistock += -1

    else:
        print("Sorry, that item does not exist.")

checkthreedigit()


amount_inserted = float(input("Please insert amount due: "))
if amount_inserted > 1.00:
    change = amount_inserted - 1.00
    print(f"Your change of ", + change, " now being dispensed")
elif amount_inserted < 1.00:
    while amount_inserted < 1.00:
        amount_inserted = amount_inserted + float(input("Please insert amount due: "))
    print("Change is now being dispensed.")
else:
    print("Item now being dispensed.")
    
    
    


