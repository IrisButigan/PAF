#Zadatak 1 (a)
a = 5.0
b = 4.935
print(a-b)
#Očekujemo rezultat 0.065, ali dobili smo 0.06500000000000039. 
#To se događa jer razliku brojeva a i b ne možemo zapisati u obliku potencije 1/2^n.
#S obzirom na to, rezultat dobiven u Pythonu točan je do određene decimale nakon koje dolazi do odstupanja, tj. ovakav rezultat je aproksimacija. 

#Zadatak 1 (b)
a = 0.1
b = 0.2
c = 0.3
d = 0.6
if a+b+c == d:
    print("Jednako")
else:
    print("Nije jednako")

print(a+b+c)

#Očekivali smo rezultat 0.6, ali dobili smo 0.6000000000000001.
#Do odstupanja dolazi zbog istog razloga kao u zadatku pod a.

