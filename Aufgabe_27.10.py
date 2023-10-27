"""
-Großauftrag von 1.000 Kisten, LKW erfasst 75 Kisten pro Lieferung
-> Berechnung, wie viele Lieferungen gemacht werden müssen und wie viele Kisten die letzte Fahrt hat


gesamt_Kisten = 1000
kisten_pro_Fahrt = 75

anzahl_fahrten = (gesamt_Kisten + kisten_pro_Fahrt - 1) // kisten_pro_Fahrt
kisten_letzte_fahrt = gesamt_Kisten % kisten_pro_Fahrt

print("Es werden insgesamt", int(anzahl_fahrten), "Fahrten benötigt.")
print("Die letzte Fahrt enthält", int(kisten_letzte_fahrt), "Kisten.")
"""

"""
def do_something(x,y):
if x > 0 and x < 100 and y > 10 and y < 20:
print ("valid range")

-> Aufgabe: vereinfache den Code

def do_something(x, y):
    if x in range(1, 101) and y in range(11, 20):
        print("valid range")
    else:
        print("invalid range")    

do_something(20, 16)
do_something(101, 18)


def check_score(points, highscore):
    if points > highscore:
        print("Congratulations, this is a new highscore")
    else:
        print("Sorry, try again")    

check_score(1234, 1000)"""

def print_number_triangle(rows):
    for x in range(1, rows + 1):
        # Leerzeichen vor den Zahlen einfügen
        print(" " * (rows - x), end="")
        
        # Zahlen in aufsteigender Reihenfolge ausgeben
        for y in range(1, 2 * x):
            print(y, end="")
        
        print()  # Zeilenumbruch am Ende jeder Zeile


print_number_triangle(6) # Aufruf der Funktion mit der Anzahl der Zeilen


def print_number_pattern(rows):
    num = 1
    for x in range(1, rows + 1):
        for y in range(1, x + 1):
            print(num, end="")
            num += 1
        print()  # Zeilenumbruch am Ende jeder Zeile

# Aufruf der Funktion mit der Anzahl der Zeilen
print_number_pattern(4)
