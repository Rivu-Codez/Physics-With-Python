'''
In this code we analyse a freely falling body under the influence of gravity.
We will use Euler's method to solve the differential equation of motion for a body in 
free fall.The acceleration due to gravity is assumed to be constant, 
and air resistance is neglected.
'''

import numpy as np
import matplotlib.pyplot as plt
import math
#DEFINING VARIABLES AND CONSTANT g = 9.81 m/s^2
t = np.linspace(0, 10, 100)
v_0 = 0
g = 9.81
x_0 = v_0*t + 0.5*g*t**2

#POSITION TIME GRAPH OF A PARTICLE UNDER FREE FALL
plt.plot(t, x_0)
plt.title('Ideal Free Fall')
plt.xlabel('Time(s)')
plt.ylabel('Position(m)')
plt.show()

#VELOCITY TIME GRAPH OF A PARTICLE UNDER FREE FALL
v = v_0 + g*t
plt.plot(t, v)
plt.title('Velocity vs Time')
plt.xlabel('Time(s)')
plt.ylabel('Velocity(m/s)')
plt.show()

