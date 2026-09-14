from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
x,y = meshgrid(arange(-5,5,0.1), arange(-5,5,0.1))
z=x**2+y**2   # this is an example to understand the syntax, not the function of the exercise
ax=figure3D()
ax.plot_surface(x,y,z)
fig=figure()
contour(x,y,z)
fig=figure()
x,y=meshgrid(arange(-5,5,0.5), arange(-5,5,0.5))
quiver(x,y,2*x,2*y)
pause(10)

