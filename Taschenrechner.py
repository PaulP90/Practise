rechenzeichen = input("Addieren?(+), Subtrahieren?(-), Dividieren?(/), Multiplizieren?(*)")
ergebnis = 0

a = int(input("1. Zahl:"))
b = int(input("2. Zahl:"))

if rechenzeichen == "+":
    ergebnis = a+b

if rechenzeichen == "-":
    ergebnis = a-b

if rechenzeichen == "/":
    ergebnis = a/b

if rechenzeichen == "*":
    ergebnis = a*b

print("Das Ergebnis lautet:", ergebnis)