#aanmaken van de lijst
getallen = []
#vullen van de lijst
for i in range(1,11):
    invoer = int(input())
    getallen.append(invoer)
print(getallen,sum(getallen))#sum geeft de som van een lijst
print("de getallen zijn {} de som van de lijst is {}".format(getallen,sum(getallen)))
