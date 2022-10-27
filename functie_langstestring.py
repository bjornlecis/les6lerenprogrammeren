def langste_string(string1, string2):
    if len(string1) > len(string2):
        print("String 1 is langer")
    elif len(string1) < len(string2):
        print("String 2 is langer")
    else:
        print("Beide strings zijn even lang")

naam1 = input("geef naam in")
naam2 = input("geef naam in")
langste_string(naam1,naam2)
langste_string("Jan","Piet")
