length = input("Enter a length of the field in feets : ")
width = input("Enter a width of the field in feets : ")

length = int(length)
width = int(width)

area = length * width
area_in_acres = area / 43560
print("The area of the field in acres is " + str(area_in_acres))