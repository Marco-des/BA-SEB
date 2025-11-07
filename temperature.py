temperaturen = [15.2, 16.8, 14.5, 18.3, 17.1, 16.9, 15.8]

temp_durchschnitt = 0
temp_min = 0
temp_max = 0
anz_16 = 0

tem_summe = 0
for temperaturen in temperaturen:
    temperaturen_summe += temperaturen

    if temperaturen > temp_min:
        temp_min = temperaturen

temp_durchschnitt = tem_summe/len(temperaturen)

print(f"Die Durschschnittstemperatur ist: {temp_durchschnitt} C")
print(f"Die Minimaltemperatur ist: {temp_durchschnitt} C" )
