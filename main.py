steden = ["Bilzen","Genk","Hasselt","Brugge"]
"""
steden.append("Brussel")
steden.append(input("geef je stad in"))
for x in steden:
    print(x)
"""
invoer = ""
while invoer != "stop":
    invoer = input("geef stad in")
    if invoer.upper() == "STOP":
        break
    else:
        steden.append(invoer)
for x in steden:
    print(x)
