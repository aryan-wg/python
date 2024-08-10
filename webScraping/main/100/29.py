from math import pi
def clac_vol(h):
    r = 10
    return (((4*pi*(r**3))/3)-(pi*(h**2)*(3*r-h))/3)

h = input("enter height \n")
print(clac_vol(int(h)))
