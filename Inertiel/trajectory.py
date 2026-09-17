from roblib import *

dt = 0.5
tmax = 6
ax = init_figure(-1.5, 1.5, -1.5, 1.5)

E1 = array([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
E2 = array([[0, 0, 0], [0, 0, 1], [0, 0, 0]])
E3 = array([[0, -1, 0], [1, 0, 0], [0, 0, 0]])

def simu_truth():
    for t in arange(0, tmax, dt):
        x1 = cos(t)
        x2 = sin(t)
        x3 = pi/2 + t
        draw_tank(array([[x1], [x2], [x3]]), 'green', 0.05)
        pause(0.01)

def simu_Euler(x1, x2, x3, u1, u2):
    for t in arange(0, tmax, dt):
        draw_tank(array([[x1], [x2], [x3]]), 'darkblue', 0.05)
        dx1, dx2, dx3 = u1*cos(x3), u1*sin(x3), u2
        x1, x2, x3 = x1 + dt*dx1, x2 + dt*dx2, x3 + dt*dx3

def simu_Lie(x1, x2, x3, u1, u2):
    p = pose(x1, x2, x3)
    for t in arange(0, tmax, dt):
        x1, x2, x3 = invpose(p)
        draw_tank(array([[x1], [x2], [x3]]), 'red', 0.05)
        p = p @ expm(dt * (u1*E1 + u2*E3))
        pause(0.1)

def pose(x1, x2, x3):
    return array([[cos(x3), -sin(x3), x1], [sin(x3), cos(x3), x2], [0, 0, 1]])

def invpose(p):
    x1 = p[0, 2]
    x2 = p[1, 2]
    x3 = arctan2(p[1, 0], p[0, 0])
    return x1, x2, x3
    
simu_truth()
simu_Euler(1, 0, pi/2, 1, 1)
pause(2)
simu_Lie(1, 0, pi/2, 1, 1)
pause(1000)