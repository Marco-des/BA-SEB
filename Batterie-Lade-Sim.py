"""Aufgabe zur Vorlesung 4 Batterie Lade Simulation mit
Start   3.0 V
Ziel    4.2 V
Sicherheitslimit 4.5 V
Spannung pro Zyklus 0.1 V max. 50 Zyklen
"""

ladung = 3.0
zyklus = 0

for zyklus in range(1,50):
    ladung = ladung + 0.1
    zyklus += 1
    if zyklus %5 == 0:
        print(f"Die Ladung ist bei {ladung}")
    if ladung == 4.2:
        break
    if ladung == 4.5:
        break
    if zyklus == 50:
        break
    
    print(f"""Die Ladung ist bei {ladung} 
Der Zyklus bei {zyklus}""")