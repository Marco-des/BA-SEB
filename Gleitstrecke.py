"""Skript für Funktion zur Berechung der Gleitstrecke eines Segelflugzeugs"""

def gleitstrecke(starthöhe, höhenverlust, höhenreserve):
    """Funktion zur Berechnug der Gleitstrecke eines Segelflugzeugs
    
    Eingabe:
    Starthöhe in Metern
    Höhenverlust pro Kilometer in Metern m/km
    Höhenreserve in Metern

    Ausgabe:
    max. Gleitstrecke in km
    """
    flughoehe = starthöhe - höhenreserve
    if flughoehe < 0:
            return None
    strecke = flughoehe / höhenverlust
    return strecke

def gleitstrecke_ausgabe():
        print(f"Die Gleitstrecke ist {gleitstrecke: 2f} km")

def main():
      eingabe_starthoehe = float (input("Starthoehe in m:"))
      eingabe_hoehenverlust = float (input("Welchen Hoehenverlust in m/km:"))
      eingabe_hoehenreserve = float (input("Welche Hoehenreserve in m"))

      strecke = gleitstrecke(eingabe_starthoehe, eingabe_hoehenverlust, eingabe_hoehenreserve)
      gleitstrecke_ausgabe9(strecke)

main()