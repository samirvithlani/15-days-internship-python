country ={"+91":"India","+1":"Us"}

for i in country:
    print(i,":",country.get(i))

print(country.items())    

print(country.get("+91"))

for I in country.values():
     print(I)

