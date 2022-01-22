#Gets business data to create an estimate
companySize = int(input("Company size: "))
productTier = int(input("Product tier (1, 2, 3): "))
securityTier = int(input("Security tier (1, 2, 3): "))

basePrice = 999.99


#Company size
if companySize in range (0, 99):
    size = "a"
    sizeMultiplier = 1

elif companySize in range (100, 999):
    size = "b"
    sizeMultiplier = 0.5

else:
    size= "c"
    sizeMultiplier = 1

#Product tier 
if productTier == 1:
    tierFee = 0
elif productTier == 2:
    tierFee = 500
elif productTier == 3:
    tierFee = 1000
else:
    print("Not an option!")

#Security tier
if securityTier == 1:
    securityFee = 0
elif securityTier == 2:
    securityFee = 250
elif securityTier == 3:
    securityFee = 500


#Prints quote
sizeFee = basePrice * sizeMultiplier
total = basePrice + sizeFee + tierFee + securityFee

print("base price = " + str(basePrice))
print("---------------")
print("size fee = " + str(sizeFee))
print("tier fee = " + str(tierFee))
print("security fee = " + str(securityFee))
print("--------------")
print("total = " + str(total))