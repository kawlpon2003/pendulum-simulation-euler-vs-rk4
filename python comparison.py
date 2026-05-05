#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81
L = 1.0
b = 0.2
dt = 0.02
t_max = 10

t = np.arange(0, t_max, dt)

# ---------------- EULER METHOD ----------------
theta = 0.8
omega = 0.0

theta_euler = []

for _ in t:
    alpha = -(g/L) * np.sin(theta) - b * omega
    omega += alpha * dt
    theta += omega * dt
    theta_euler.append(theta)

theta_euler = np.array(theta_euler)

# ---------------- RK4 METHOD ----------------
theta = 0.8
omega = 0.0

theta_rk4 = []

def derivatives(theta, omega):
    return omega, -(g/L)*np.sin(theta) - b*omega

for _ in t:
    k1_t, k1_o = derivatives(theta, omega)
    k2_t, k2_o = derivatives(theta + 0.5*dt*k1_t, omega + 0.5*dt*k1_o)
    k3_t, k3_o = derivatives(theta + 0.5*dt*k2_t, omega + 0.5*dt*k2_o)
    k4_t, k4_o = derivatives(theta + dt*k3_t, omega + dt*k3_o)

    theta += (dt/6)*(k1_t + 2*k2_t + 2*k3_t + k4_t)
    omega += (dt/6)*(k1_o + 2*k2_o + 2*k3_o + k4_o)

    theta_rk4.append(theta)

theta_rk4 = np.array(theta_rk4)

# ---------------- COMPARISON PLOT ----------------
plt.figure()

plt.plot(t, theta_euler, '--', label='Euler')
plt.plot(t, theta_rk4, '-', label='RK4')

plt.xlabel("Time (s)")
plt.ylabel("Theta (rad)")
plt.title("Euler vs RK4 Comparison")
plt.legend()
plt.grid()

plt.savefig("comparison.png")
plt.show()


# In[ ]:




