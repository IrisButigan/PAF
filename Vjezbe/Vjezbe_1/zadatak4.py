def pravac(x1, y1, x2, y2):
    if x1 != x2:
        a = (y2 - y1)/(x2 - x1)
        b = - a * x1 + y1
        print("Pravac y = {}x + {}".format(a, b))
    else:
        print("Pravac x = {}".format(x1))

pravac(1,2,3,4)