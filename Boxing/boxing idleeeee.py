from pyfiglet import Figlet
f = Figlet (font=("larry3d"))

#variable declartion
priceRedGloves = 35
priceHeadgear = 50
priceMouthguard = 10
priceGroingaurd = 40

quantityRedGloves = 0
quantityHeadgear = 0
quantityMouthguard = 0
quantityGroingaurd = 0

SubTotalRedGloves = 0
SubTotalHeadgear = 0
SubTotalMouthguard = 0
SubTotalGroingaurd = 0
extrapadding = "YES"
extraGroingaurd = "YES"
Itemcounter = 0
print(f.renderText("Welcome to my boxing store"))

grandTotal = 0

while True:
    Firstname = input("please enter your name: ")
    if len(Firstname) > 0:
        print("Welcome to my boxing store")
        break


FirstName = input("Please enter your name")
print("Nice to meet you", FirstName)
postcode = input("please enter your postcode for delivery")
print("your eligble for delivery")
ordertype = input("do you want delivery or collection:")
if ordertype == "Delivery":
    postcode = input ("please enter your postcode:")
    steertName = input("please enter your street name:")
    doorno = input ("please enter your door number:")
elif ordertype == "Collection":
    postcode = input ("Please enter your postcode to find nearest store next to you:")
    postcode = print ("Collection is available after 24 hours")
    




print("1.RedGloves - £35")
print("2.Headgear - £50")
print("3.Mouthgaurd - £10")
print("4.Groingaurd - £40")

choice = int(input("Please choose a gear from the menu:"))
if choice == 1:
    Itemcounter +=1
    print(" You have selected RedGloves - 35")
    quantityRedGloves = int(input("how many copies would you like"))
    SubTotalRedGloves = priceRedGloves * quantityRedGloves
    print("Your total cost is",SubTotalRedGloves)

    extrapadding = input("would you like extra padding to your gloves")

    SubTotalRedGloves = priceRedGloves * quantityRedGloves
    
    if extrapadding.upper() == "YES":
         SubTotalRedGloves += 20 * quantityRedGloves

    
    
elif choice == 2:
    Itemcounter +=1
    print("You have selected Headgear - 50")
    quantityHeadgear = int(input("how many copies would you like"))
    SubtotalHeadgear = priceHeadgear * quantityHeadgear
    print("Your total cost is",SubTotalHeadgear)

    extrapadding = input("would you like extra padding to your Headgear")
    SubTotalHeadgear = priceHeadgear * quantityHeadgear

    if extrapadding.upper() == "YES":
        SubTotalHeadgear += 20* quantityHeadgear
    
    
elif choice == 3:
    Itemcounter +=1
    print("You have selected Mouthguard - 10")
    quantityMouthguard = int(input("how many copies would you like"))
    SubTotalMouthguard = priceMouthguard * quantityMouthguard
    print("Your total cost is",SubTotalMouthguard)

    extraMouthguard = input("would you like an extra Mouthguard")
    SubTotalMouthguard = priceMouthguard * quantityMouthguard

    if extraMouthguard.upper() == "YES":
         SubTotalMouthguard += 20* quantityMouthguard

     
 
elif choice == 4:
    Itemcounter +=1
    print("your have selected Groingaurd - 40")
    quantityGroingaurd = int(input("how many copies would you like"))
    SubTotalGroingaurd = priceGroingaurd * quantityGroingaurd
    print("Your total cost is",SubTotalGroingaurd)

    extrapadding = input("would you like extra padding to your Groingaurd")
    SubTotalGroingaurd = priceGroingaurd * quantityGroingaurd

    if extraGroingaurd.upper() == "YES":
        SubTotalGroingaurd += 20* quantityGroingaurd
        

    
    

    
 


grandTotal = SubTotalRedGloves + SubTotalHeadgear + SubTotalMouthguard + SubTotalGroingaurd

print("Reciept")
print("------------------------------------------------------------------------------------------------------------------------------->")
print("Thank you for shopping with us" , FirstName)
print("Item Name:         PRICE:             QUANTITY             SUBTOTAL")
if quantityRedGloves > 0:
    print("RedGloves          ",priceRedGloves,"             ",quantityRedGloves,"              ",SubTotalRedGloves)
if quantityHeadgear > 0:
     print("Headgear        , ",priceHeadgear,"             ",quantityHeadgear,"              ",SubTotalHeadgear)
if quantityMouthguard > 0:
    print("Mouthgaurd         ",priceMouthguard,"             ",quantityMouthguard,"              ",SubTotalMouthguard)
if quantityGroingaurd> 0:
    print("Groingaurd         ",priceGroingaurd,"             ",quantityGroingaurd,"              ",SubTotalGroingaurd)
    print("--------------------------------------------------------------------------------------------------------------------------->")
    paymentMethod = input("Will you be paying cash or card").lower()
    if paymentMethod == "cash":
        print("Please pay", grandTotal)
        
        
    
    
        
        
        
    
    


