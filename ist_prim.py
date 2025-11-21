def ist_prim(zahl):
    """Gibt aus, ob `zahl` eine Primzahl ist."""
    if zahl == 1:
        return False
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            return False
        if teiler**2 > zahl:
            break
    return True