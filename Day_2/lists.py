fav=["bahubali","love","96","cricket","swimming"]
print(fav[0])
print(fav[-1])
fav.append("Gym")
print(len(fav))
for i in fav:
    print(i)

exis=["Limitation","Facticity","expectation","ocd","bond"]
exis[1]="love"
print(exis[::1])
exis.remove("love")
exis.pop()
print(exis[::1])
print(len(exis))