try:
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
except:
    print("Pogreška unosa. Pokušajte ponovno.")
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))

##y - y1 = y2 - y1 / x2 - x1 (x - x1)
if x1 != x2:
    a = (y2 - y1)/(x2 - x1)
    b = - a * x1 + y1
    print("Pravac y = {}x + {}".format(a, b))
else:
    print("Pravac x = {}".format(x1))