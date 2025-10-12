#Schwebedauer Multikopter
#Eingabe m in g, Anzahl in n, Duurchmesser in 2r in m

k = 0.5 #dimensionslose Effizienz
g = 9.81 #Erdbeschleunigung in m/s^2
Kap = 3.0 #Kapazität in Ah
U = 11.1 #Spannung in V
p = 1.2 #Luftdichte (München) in kg/m^3

m = float(input("Geben Sie die Masse des Roboters in g an: "))
n = int(input("Geben Sie die Anzahl der Rotoren an: "))
d = float(input("Geben Sie den Durchmesser der Rotoren in m an: "))
r = d/2 #Radius in m

m = m/1000 #Masse in kg

T = m*g #Gewichtskraft in N
A = n*3.14*r**2 #Gesamtfläche der Rotoren in m^2
P = (T**1.5)/((2*p*A)**0.5) #Leistung in W
E = Kap*U*3600 #Energie in Ws
t = E/P #Schwebedauer in s  

print("Die Schwebedauer beträgt", round(t,2), "s")