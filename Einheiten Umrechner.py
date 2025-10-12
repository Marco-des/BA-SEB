#Einheiten Umrechner

einheit = input("Welche Einheit möchten Sie umrechnen? (f, NM, kn: ")

if einheit == "f":
    f = float(input("Geben Sie die Anzahl der Fuß ein: "))
    m = f * 0.3048
    print(f"{f} Fuß sind {m:.2f} Meter.")
elif einheit == "NM":
    nm = float(input("Geben Sie die Anzahl der Seemeilen ein: "))
    m2 = nm * 1852
    print(f"{nm} Seemeilen sind {m2:.2f} Meter.")
elif einheit == "kn":
    kn = float(input("Geben Sie die Anzahl der Knoten ein: "))
    m3 = kn * 0.514444
    print(f"{kn} Knoten sind {m3:.2f} Meter pro Sekunde.")
else:
    print("Ungültige Einheit. Bitte wählen Sie 'f', 'NM' oder 'kn'.")
