'''
In this code we analyse a freely falling body under the influence of gravity.
We will use Euler's method to solve the differential equation of motion for a body in 
free fall.The acceleration due to gravity is assumed to be constant, 
and air resistance is neglected.
'''

import numpy as np
import matplotlib.pyplot as plt
x_0 = float(input("Enter the initial height of the body (in meters): "))
v_0 = 0
g = 9.81
t_0 = 0

#Using Euler's method to solve the differential equation of motion


