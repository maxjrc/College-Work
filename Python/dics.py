thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.get('brand'))

add = input("What do you want the color to be? ")

thisdict["color"] = add

print(thisdict)

change = input("What do you want to change the color to? ")

thisdict["brand"] = change

print(thisdict)
