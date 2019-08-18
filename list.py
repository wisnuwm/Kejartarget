#List
apaaja = ["a","b","c","d","e","f"]
print(apaaja[2])

#change
apaaja[2] = "w"
print (apaaja)
for x in apaaja:
    print(x)

#cek
if "a" in apaaja:
    print("Yes, 'a' is in alfabet list")

#tambahkan item
apaaja.append("k")
print(apaaja)

#insert
apaaja.insert(1,"b")
print(apaaja)

#remove
apaaja.remove("b")
print(apaaja)