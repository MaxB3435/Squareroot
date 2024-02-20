import matplotlib.pyplot as plt
import numpy as np
def square_root(a, epsilon):
    if a < 0:
        return 'Error'
    else:
        h = max(1,a)
        l = 0
        b = (h+l)/2
        while abs(b*b - a) >= epsilon:
            if b*b < a:
                l = b
            else:
                h = b
            b = (h+l)/2
        return b
     
print(square_root(2,0.01))
