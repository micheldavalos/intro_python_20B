temp = int(input("Temp:"))
if temp <= 0:
    print("Está helado")
elif temp > 0 and temp <= 12:
    print("Está frío")
elif temp > 12 and temp <= 18:
    print("No está tan frío")
elif temp > 18 and temp <= 24:
    print("Está calido")
else:
    print("Esta caluroso")