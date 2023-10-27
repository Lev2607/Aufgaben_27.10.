"""
-Großauftrag von 1.000 Kisten, LKW erfasst 75 Kisten pro Lieferung
-> Berechnung, wie viele Lieferungen gemacht werden müssen und wie viele Kisten die letzte Fahrt hat
"""

gesamt_Kisten = 1000
kisten_pro_Fahrt = 75

anzahl_Fahrten = gesamt_Kisten / kisten_pro_Fahrt
kisten_letzte_fahrt = gesamt_Kisten % kisten_pro_Fahrt

print("Es werden insgesamt", int(anzahl_Fahrten), "Fahrten benötigt.")
print("Die letzte Fahrt enthält", int(kisten_letzte_fahrt), "Kisten.")