from polygon import *
poly1 = Polygon()
poly2 = Polygon(8, 5)

print("Polygon 1: ")
print("     # of sides:         ", poly1.get_n())
print("     length of a side:   ", poly1.get_side())
print("     Area:                %.2f" %poly1.get_area())
print("     Perimeter:          ", poly1.get_perimeter())

print("Polygon 2: ")
print("     # of sides:         ", poly2.get_n())
print("     length of a side:   ", poly2.get_side())
print("     Area:                %.2f" %poly2.get_area())
print("     Perimeter:          ", poly2.get_perimeter())
