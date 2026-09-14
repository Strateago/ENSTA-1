from sympy import *

def Symb_build():
    t = symbols('t')
    mr,mc,g,l= symbols('mr mc g l')
    u = Function('u')('t')


from roblib import *

def draw_invpend(ax,x,col='blue'): #inverted pendulum
    s,θ=x[0,0],x[1,0]
    draw_box(ax,s-0.7,s+0.7,-0.25,0,col)
    plot( [s,s-sin(θ)],[0,cos(θ)],'magenta', linewidth = 2)


mc,l,g,mr=5,1,9.81,1
x = array([[0,2,0,0]]).T
ax=init_figure(-3,3,-3,3)
draw_invpend(ax,x)
pause(1)

