# оушен
# нбибд 01-24
# лаб 2
# python
# задача 1
import math

def has_real_roots(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        return True 
    else:
        return False 
has_real_roots(1, -3, 2)
