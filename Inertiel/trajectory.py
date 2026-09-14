from roblib import *

dt = 0.5
tmax = 6
ax = init_figure(-1.5, 1.5, -1.5, 1.5)

def simu_truth():
    for t in arange(0, tmax, dt):
        x1 = cos(t)
        x2 = sin(t)
        x3 = pi/2 + t
        draw_tank(array([[x1], [x2], [x3]]), 'green', 0.05)

def simu_Euler(x1, x2, x3, u1, u2):
    for t in arange(0, tmax, dt):
        draw_tank(array([[x1], [x2], [x3]]), 'darkblue', 0.05)
        dx1, dx2, dx3 = u1*cos(x3), u1*sin(x3), u2
        x1, x2, x3 = x1 + dt*dx1, x2 + dt*dx2, x3 + dt*dx3

simu_truth()
simu_Euler(1, 0, pi/2, 1, 1)