# Establishing all global variables that will be used in each function in the Vending Machine program.

#Variable wherein the 3 digit code the user will use to specify their chosen product will be stored.
threedigit = 000

# Variables to be used within the money change system.
amount_inserted = 0.00
amount_due = 0.00

# Variables to be used as stock trackers for all products in the vending machine.
maidubaistock = 3
fijistock = 3
Al_Ainstock = 3
Coca_Colastock = 3
Pepsistock = 3
Mountain_Dewstock = 3
sevenUpstock = 3
Coke_Zerostock = 3
dietpepsistock = 3
Gatoradestock =3 
Monster_Energystock = 3
Celcius_Live_Fitstock = 3
Red_Bull_Zerostock = 3
MnMstock = 3
MnM_Peanutsstock = 3
Reeses_Piecesstock = 3
KitKat_Four_Fingerstock =3 
skittlesstock = 3
Snickersstock = 3
Hersheys_CnCreamstock = 3
Nestles_Milky_Barstock = 3


# Function in the form of a money change system.
# Uses global variable "amount_due" whose value (price) will depend on the item the user chooses.
def change_system():
    global amount_due

# Variable (float) "amount_inserted" will be put against variable "amount due" which will decide which block will be triggered.
    amount_inserted = float(input("Please insert amount due: "))

# If amount inserted is greater than amount due, the program will subtract the price of the chosen 
# item from the users inputted money, resulting in the right amount of change to be given back.
    if amount_inserted > amount_due:
        amount_inserted = amount_inserted - amount_due
        print(f"Your item and change of", + amount_inserted, "now being dispensed.")
        amount_inserted = 0.00  
        amount_due = 0.00 
        buyanother() 

# If amount inserted is less than amount due, the user will continuously be asked to give money
# until the total amount inserted equals or exceeds the amount due. If during this process the
# sum total of money inserted exceeds the amount due, it will also give the necessary change.
    elif amount_inserted < amount_due:
        while amount_inserted < amount_due:
            amount_inserted = amount_inserted + float(input("Please insert amount due: "))
            if amount_inserted > amount_due:
                amount_inserted = amount_inserted - amount_due
                print(f"Your item and change of", + amount_inserted, "now being dispensed.")
                amount_inserted = 0.00
                buyanother()
        print("Item is now being dispensed.")
        amount_inserted = 0.00
        amount_due = 0.00
        buyanother()

# If however the user gives the exact amount of money needed, the program will straightaway give the item without any change.
    else:
        print("Item now being dispensed.")
        amount_inserted = 0.00
        amount_due = 0.00 #The value of the used variables are then reset to accomodate the next order.
        buyanother() #The user is then given a prompt (using a defined variable) to ask if they want to order again.



# Function to ask the user for a 3 digit code that will determine what item will be given.
def checkthreedigit():

# Global variables to be used:
    global threedigit  # variable where the 3 digit code will be stored
    global amount_inserted  # variable where users money will be stored and what amount due will be subtracted against.
    global amount_due # the price needed to be met in order to give the item, its value is determined by the item the user chooses.
    
# Global variables to be used as stock trackers, if this number reaches 0, the user will be informed that no more of that item can be given.
    global maidubaistock
    global fijistock
    global Al_Ainstock
    global Coca_Colastock
    global Pepsistock
    global Mountain_Dewstock
    global sevenUpstock
    global Coke_Zerostock
    global dietpepsistock
    global Gatoradestock
    global Monster_Energystock
    global Celcius_Live_Fitstock
    global Red_Bull_Zerostock
    global MnMstock
    global MnM_Peanutsstock
    global Reeses_Piecesstock
    global KitKat_Four_Fingerstock
    global skittlesstock
    global Snickersstock
    global Hersheys_CnCreamstock
    global Nestles_Milky_Barstock


    threedigit = input("Please Enter the 3-Digit Number of Your Chosen Product: ")

    if threedigit == "101":   #if elif block that checks which 3 digit code; which item the user wants.

        if maidubaistock > 0:    #if elif chain within main loop that checks if item is in stock.

            amount_due = amount_due + 1.00   #sets the amount due; money needed to be matched in order to give item.

            maidubaistock += -1   #code to subtract 1 unit from the item's stock tracker.

            amount_inserted = amount_inserted + 1.00   #code to set the amount needed to be inserted by the user.

            change_system() #calling the function that calculates change needed to be given.

        elif maidubaistock == 0:   #block of code that triggers once the amount of stock of a specific item reaches 0.

            print("Sorry this item is out of stock.")     #Prompts the user that their item of choice is out of stock.

            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen : " ) 
            #Asks the user to either go back to menu to buy something else or quit to terminate the process.
            #if elif chain to direct flow to either the menu screen or start screen.
            if backtomenu == "Menu":

                menu() #Calling menu function.

            elif backtomenu == "Quit":
               
               start_screen() #Calling start screen function.

               

    elif threedigit == "102":
        if fijistock > 0:
            amount_due = amount_due + 8.55
            fijistock += -1
            amount_inserted = amount_inserted + 8.55
            change_system()
        elif fijistock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    #elif blocks for each of the remaining items.
    elif threedigit == "103":
        if Al_Ainstock > 0:
          amount_due = amount_due + 1.00
          Al_Ainstock += -1
          amount_inserted = amount_inserted + 1.00
          change_system()
        elif Al_Ainstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()


    elif threedigit == "104":
        if Coca_Colastock > 0:
          amount_due = amount_due + 3.50
          Coca_Colastock += -1
          amount_inserted = amount_inserted + 3.50
          change_system()
        elif Coca_Colastock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "105":
        if Pepsistock > 0:
          amount_due = amount_due + 3.50
          Pepsistock += -1
          amount_inserted = amount_inserted + 3.50
          change_system()
        elif Pepsistock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "106":
        if Mountain_Dewstock > 0:
          amount_due = amount_due + 3.50
          Mountain_Dewstock += -1
          amount_inserted = amount_inserted + 3.50
          change_system()
        elif Mountain_Dewstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()
          
    elif threedigit == "107":
        if sevenUpstock > 0:
          amount_due = amount_due + 3.50
          sevenUpstock += -1
          amount_inserted = amount_inserted + 3.50
          change_system()
        elif sevenUpstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()
       
    elif threedigit == "108":
        if Coke_Zerostock > 0:
          amount_due = amount_due + 5.00
          Coke_Zerostock += -1
          amount_inserted = amount_inserted + 5.00
          change_system()
        elif Coke_Zerostock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "109":
        if dietpepsistock > 0:
          amount_due = amount_due + 5.00
          dietpepsistock += -1
          amount_inserted = amount_inserted + 5.00
          change_system()
        elif dietpepsistock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "110":
        if Gatoradestock > 0:
          amount_due = amount_due + 5.00
          Gatoradestock += -1
          amount_inserted = amount_inserted + 5.00
          change_system()
        elif Gatoradestock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "111":
        if Monster_Energystock > 0:
          amount_due = amount_due + 1.00
          Monster_Energystock += -1
          amount_inserted = amount_inserted + 1.00
          change_system()
        elif Monster_Energystock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "112":
        if Celcius_Live_Fitstock > 0:
          amount_due = amount_due + 8.00
          Celcius_Live_Fitstock += -1
          amount_inserted = amount_inserted + 8.00
          change_system()
        elif Celcius_Live_Fitstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()


    elif threedigit == "113":
        if Red_Bull_Zerostock > 0:
          amount_due = amount_due + 9.60
          Red_Bull_Zerostock += -1
          amount_inserted = amount_inserted + 9.60
          change_system()
        elif Red_Bull_Zerostock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()


    elif threedigit == "201":
        if MnMstock > 0:
          amount_due = amount_due + 3.80
          MnMstock += -1
          amount_inserted = amount_inserted + 3.80
          change_system()
        elif MnMstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()


    elif threedigit == "202":
        if MnM_Peanutsstock > 0:
          amount_due = amount_due + 4.00
          MnM_Peanutsstock += -1
          amount_inserted = amount_inserted + 4.00
          change_system()
        elif MnM_Peanutsstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "203":
        if Reeses_Piecesstock > 0:
          amount_due = amount_due + 3.30
          Reeses_Piecesstock+= -1
          amount_inserted = amount_inserted + 3.30
          change_system()
        elif Reeses_Piecesstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "204":
        if KitKat_Four_Fingerstock > 0:
          amount_due = amount_due + 2.70
          KitKat_Four_Fingerstock += -1
          amount_inserted = amount_inserted + 2.70
          change_system()
        elif KitKat_Four_Fingerstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "205":
        if skittlesstock > 0:
          amount_due = amount_due + 2.75
          skittlesstock += -1
          amount_inserted = amount_inserted + 2.75
          change_system()
        elif skittlesstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "206":
        if Snickersstock > 0:
          amount_due = amount_due + 3.15
          Snickersstock += -1
          amount_inserted = amount_inserted + 3.15
          change_system()
        elif Snickersstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "207":
        if Hersheys_CnCreamstock > 0:
          amount_due = amount_due + 3.80
          Hersheys_CnCreamstock += -1
          amount_inserted = amount_inserted + 3.80
          change_system()
        elif Hersheys_CnCreamstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

    elif threedigit == "208":
        if Nestles_Milky_Barstock > 0:
          amount_due = amount_due + 1.30
          Nestles_Milky_Barstock += -1
          amount_inserted = amount_inserted + 1.30
          change_system()
        elif Nestles_Milky_Barstock == 0:
            print("Sorry this item is out of stock.")
            backtomenu = input("Enter 'Menu' to Go Back to Menu | 'Quit' to Go to Start Screen." )
            if backtomenu == "Menu":
                menu()
            elif backtomenu == "Quit":
               start_screen()

               
    else:
        print("Sorry, that item does not exist.")
        checkthreedigit()


# Dictionary of the complete menu; product name and price as key, 3 digit code assigned as value. Used in the menu() function.
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

# Dicitonaries below specifically contain items within a certain category (for use in the filter system)
drinks = {"Mai Dubai         AED 1.00":  "101",
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
          "Red Bull Zero     AED 9.60":  "113",}

lowcalorie = {"Mai Dubai         AED 1.00":  "101",
              "Fiji              AED 8.55":  "102",
              "Al Ain            AED 1.00":  "103",
              "Coke Zero         AED 5.00":  "108",
              "Diet Pepsi        AED 5.00":  "109",
              "Celcius Live Fit  AED 8.00":  "112",
              "Red Bull Zero     AED 9.60":  "113",}

water = {"Mai Dubai         AED 1.00":  "101",
         "Fiji              AED 8.55":  "102",
         "Al Ain            AED 1.00":  "103",}

softdrinks = {"Coca-Cola         AED 3.50":  "104",
              "Pepsi             AED 3.50":  "105",
              "Mountain Dew      AED 3.50":  "106",
              "7Up               AED 3.50":  "107",
              "Coke Zero         AED 5.00":  "108",
              "Diet Pepsi        AED 5.00":  "109",}

energydrinks = {"Gatorade          AED 5.00":  "110",
                "Monster Energy    AED 1.00":  "111",
                "Celcius Live Fit  AED 8.00":  "112",
                "Red Bull Zero     AED 9.60":  "113",}

snacks = {"M&M               AED 3.80":  "201",
          "M&M Peanuts       AED 4.00":  "202",
          "Reese's Pieces    AED 3.30":  "203",
          "KitKat 4 Finger   AED 2.70":  "204",
          "Skittles          AED 2.75":  "205",
          "Snickers          AED 3.15":  "206",
          "Hersheys C&Cream  AED 3.80":  "207",
          "Nestles Milky Bar AED 1.30":  "208"}

whitechocolate = {"Hersheys C&Cream  AED 3.80":  "207",
                  "Nestles Milky Bar AED 1.30":  "208"}

containsnuts = {"M&M               AED 3.80":  "201",
                "M&M Peanuts       AED 4.00":  "202",
                "Reese's Pieces    AED 3.30":  "203",
                "Snickers          AED 3.15":  "206"}

nutfree = {"KitKat 4 Finger   AED 2.70":  "204",
           "Skittles          AED 2.75":  "205",
           "Nestles Milky Bar AED 1.30":  "208"}

# Functions to print menus of a certain category which the user chooses.
def menu_drinks(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in drinks.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    checkthreedigit()

def menu_lowcalorie(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in lowcalorie.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    checkthreedigit()

def menu_water(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in water.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    checkthreedigit()

def menu_softdrinks(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in softdrinks.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    checkthreedigit()

def menu_energydrinks(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in energydrinks.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    checkthreedigit()

def menu_snacks(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in snacks.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    checkthreedigit()

def menu_whitechocolate(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in whitechocolate.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    checkthreedigit()

def menu_containsnuts(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in containsnuts.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    checkthreedigit()

def menu_nutfree(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in nutfree.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    checkthreedigit()

# Function that asks user if they want to buy another item, if yes, they will be directed back to the menu screen.
# And if not, the program is reset and goes back to start screen.
def buyanother():
    buyagain = input("Would you like to buy another item? YES or NO: ")
    if buyagain == "YES":
       menu()
    if buyagain == "yes":
       menu()
    else:
        start_screen()

# Filter Display function that (*if user opts to use) shows the user all filter options available and also asks for a filter to be used
def filtermsg():
    print(" _________________________________________")
    print("|   Which Filter Would You Like to Use?   |")
    print("|                                         |")
    print("|      Drinks            Low Calorie      |")
    print("|  Water     Softdrinks     Energy Drinks |")
    print("|                                         |")
    print("|                  Snacks                 |")
    print("|White Chocolate   Contains Nuts  Nut-Free|")
    print("|_________________________________________|")
    filterloop()


def filterloop():   # Function that prompts the user to enter a filter among the ones shown to the user in previous function "filtermsg()"
    chosenfilter = input("Please Enter The Filter You Want to Use: ")

# if elif-else-chain that directs user to filtered menu that they choose.
    if chosenfilter == "Drinks":
        menu_drinks()
    elif chosenfilter == "Low Calorie":
        menu_lowcalorie()
    elif chosenfilter == "Water":
        menu_water()
    elif chosenfilter == "Softdrinks":
        menu_softdrinks()
    elif chosenfilter == "Energy Drinks":
        menu_energydrinks()
    elif chosenfilter == "Snacks":
        menu_snacks()
    elif chosenfilter == "White Chocolate":
        menu_whitechocolate()
    elif chosenfilter == "Contains Nuts":
        menu_containsnuts()
    elif chosenfilter == "Nut-Free":
        menu_nutfree()
    else:    #else block that informs the user if what they entered is not one of the filter options.
        print("\nSorry, '", chosenfilter, "' is not an option.\n")
        filterloop()

# Function to ask if the user wants to use the filter system. 
def askfilter():
    print("\nWould you like to use a Filter?")
    filteranswer = input("Enter YES or NO: ")
    if filteranswer == "YES":
        filtermsg()
    elif filteranswer == "yes":
        filtermsg()
    else:    #If not, they are instead just asked to enter the item they would like to buy.
        checkthreedigit()

# Unfiltered Menu Function that prints out all item-code pairs from the complete menu dictionary.
def menu(): 
    print(" ______________________________________________________")
    print("|                         MENU                         |")
    print("|        ITEM              PRICE             CODE      |")
    for item, code in completemenu.items():
     print("|    ", item, " ----------- ", code, "    |")
    print("|______________________________________________________|")
    askfilter()

# Function to begin the program with a prompt telling the user to press enter to start the program.
def start_screen(): 
    print("Thank you for choosing our vending machine.")
    input("Press Enter to See Menu.")
    menu()

# Calling the function to begin the program.
start_screen()







    






  


