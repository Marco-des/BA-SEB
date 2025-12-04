"""Skript für das Würfelspiel Böse 1
    und dem Herausfinden der besten Strategie in diesem """
import random

def wuerfel():
    """Funtion, die einen 6 seitigen Würfel simuliert"""
    zufallszahl = random.randint (1, 6)
    return zufallszahl

def spiele_runde(anzahl_wuerfe):
    """Funktion, die eine Runde Würfelspiel Böse 1 simuliert.
    Input:  anzahl_wuerfe = Wie oft gewürfelt wird
    Output(Tuple): Punktzahl die in der Runwurdede erreicht, 
            liste_resultate = Liste des gewürfelten Zahlen
            """
    liste_resultate = []

    for i in range (anzahl_wuerfe):
        liste_resultate.append(wuerfel())

    if 1 in liste_resultate:
        return 0, liste_resultate
    else:
        return sum(liste_resultate), liste_resultate
    
def spiele_strategie(max_wuerfe, ziel_punkte):
    """Funktion,welche die Runden aufzählt bis man die Gewinnpunktzahl erreicht
    Input:  Max-wuerfe = Wie oft jede Runde gewürfelt wird
            ziel_punkte = Gewinnpunktzahl
    Output: Anzahl der Runde in der die Gewinnpunktzahl erreicht wurde
    """
    runde = 0
    gesamt = 0

    while gesamt <= ziel_punkte:
        runde =+ 1
        punktzahl, _ = spiele_runde(max_wuerfe)
        gesamt = gesamt + punktzahl
    return runde

def simuliere_strategie(max_wuerfe, ziel_punkte, anzahl_spiele):
    liste_runden = []
    
    for i in anzahl_spiele:
        random.seed(i)
        spiele_strategie(max_wuerfe, ziel_punkte)
        i =+ 1


def test(s):
    random.seed(s)
    wuerfel()
    spiele_runde(1)
    spiele_strategie (3,100)