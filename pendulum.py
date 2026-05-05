#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Parameters
g = 9.81
L = 1.0
m = 1.0
b = 0.2
dt = 0.02
t_max = 10

theta = 0.8
omega = 0.0

t = np.arange(0, t_max, dt)

theta_list = []
omega_list = []

# Solve motion
for _ in t:
    alpha = -(g/L) * np.sin(theta) - b * omega
    omega += alpha * dt
    theta += omega * dt
    theta_list.append(theta)
    omega_list.append(omega)

theta_list = np.array(theta_list)
omega_list = np.array(omega_list)

# Coordinates
x = L * np.sin(theta_list)
y = -L * np.cos(theta_list)

# Energy
KE = 0.5 * m * (L * omega_list)**2
PE = m * g * L * (1 - np.cos(theta_list))
E = KE + PE

# Plot setup
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_title("Pendulum")

line, = ax1.plot([], [], linewidth=2)
bob, = ax1.plot([], [], marker='o', markersize=10)

ax2.set_xlim(0, t_max)
ax2.set_ylim(0, max(E)*1.2)
ax2.set_title("Energy vs Time")

ke_line, = ax2.plot([], [], label="KE")
pe_line, = ax2.plot([], [], label="PE")
e_line, = ax2.plot([], [], label="Total")

ax2.legend()

def update(frame):
    line.set_data([0, x[frame]], [0, y[frame]])
    bob.set_data([x[frame]], [y[frame]])

    ke_line.set_data(t[:frame], KE[:frame])
    pe_line.set_data(t[:frame], PE[:frame])
    e_line.set_data(t[:frame], E[:frame])

    return line, bob, ke_line, pe_line, e_line

ani = FuncAnimation(fig, update, frames=len(t), interval=20)

plt.show()

# Save GIF
ani.save("pendulum_energy.gif", writer=PillowWriter(fps=20))


# In[ ]:




