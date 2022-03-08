from item import Item

f = open('virtualClosetData', 'a')

#itemName, itemcColor, itemMaterial, itemSeason, itemOccasion
item1 = Item(input("input type:"), input("input color:"))
f.write(item1.itemName + " , ")
f.write(item1.itemcColor + "\n")

f.close()

#print(item1.itemOccasion)

