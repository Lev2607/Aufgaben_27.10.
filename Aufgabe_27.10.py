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
"""
def do_something(x, y):
    if x in range(1, 100) and y in range(11, 20):
        print("valid range")
    else:
        print("invalid range")    

do_something(20, 16)
do_something(101, 18)
