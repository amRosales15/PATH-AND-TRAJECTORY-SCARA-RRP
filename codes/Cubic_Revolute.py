import numpy as np
import matplotlib.pyplot as plt

# degrees to radian converter
def deg_to_rad(T):
    return (T/180)*np.pi

qi = float(input('qi = ')) # initial position         0, for testing
qi = deg_to_rad(qi)

vi = float(input('vi = ')) # initial velocity         0, for testing
vi = deg_to_rad(vi)

qf = float(input('qf = ')) # final position           90,for testing
qf = deg_to_rad(qf)

vf = float(input('vf = ')) # final velocity           50, for testing
vf = deg_to_rad(vf)

ti = float(input('ti = ')) # initial time             0, for testing
tf = float(input('tf = ')) # final time               9, for testing

# Cubic
# Solve the solution for q(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

x = np.arange(ti,tf,0.05)

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

y = cubic(x,qi,qf,tf)

plt.figure()
plt.plot(x,y,'g',linestyle='-')
plt.text(1,1.5,'q(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3')
plt.grid(True)
plt.show()