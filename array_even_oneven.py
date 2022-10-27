even = []
oneven = []
for i in range(1,11):
    invoer = int(input("geef getal in"))
    if invoer%2 == 0:
        even.append(invoer)
    else:
        oneven.append(invoer)

"""
print elementen uit de lijst
for x in even: print(x)
print("-----------------")
for y in oneven: print(y)"""
#print de lijst even en oneven als list
print("even",even,type(even))
print("oneven",oneven,type(oneven))

