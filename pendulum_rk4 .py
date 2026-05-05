#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
g = 9.81
L = 1.0
m = 1.0
b = 0.2
dt = 0.02
t_max = 10

# Initial conditions
theta = 0.8
omega = 0.0

t = np.arange(0, t_max, dt)

theta_list = []
omega_list = []

# Define derivatives
def derivatives(theta, omega):
    dtheta_dt = omega
    domega_dt = -(g/L)*np.sin(theta) - b*omega
    return dtheta_dt, domega_dt

# RK4 Method
for _ in t:
    k1_theta, k1_omega = derivatives(theta, omega)
    
    k2_theta, k2_omega = derivatives(
        theta + 0.5*dt*k1_theta,
        omega + 0.5*dt*k1_omega
    )
    
    k3_theta, k3_omega = derivatives(
        theta + 0.5*dt*k2_theta,
        omega + 0.5*dt*k2_omega
    )
    
    k4_theta, k4_omega = derivatives(
        theta + dt*k3_theta,
        omega + dt*k3_omega
    )
    
    theta += (dt/6)*(k1_theta + 2*k2_theta + 2*k3_theta + k4_theta)
    omega += (dt/6)*(k1_omega + 2*k2_omega + 2*k3_omega + k4_omega)

    theta_list.append(theta)
    omega_list.append(omega)

theta_list = np.array(theta_list)
omega_list = np.array(omega_list)

# Convert to coordinates
x = L * np.sin(theta_list)
y = -L * np.cos(theta_list)

# Energy
KE = 0.5 * m * (L * omega_list)**2
PE = m * g * L * (1 - np.cos(theta_list))
E = KE + PE

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)

line, = ax1.plot([], [], linewidth=2)
bob, = ax1.plot([], [], marker='o', markersize=10)

ax2.set_xlim(0, t_max)
ax2.set_ylim(0, max(E)*1.2)

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
from matplotlib.animation import PillowWriter
ani.save("pendulum_rk4.gif", writer=PillowWriter(fps=20))


# In[ ]:





# In[ ]:




