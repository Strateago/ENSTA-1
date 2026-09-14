
from roblib import *

def draw_wheel3D(ax,x,y,z,φ,θ,ψ,r=1,col='blue',size=1):
    M=tran3H(x,y,z)@eulerH(φ,θ,ψ)@wheel3H(r)
    draw3H(ax,M,col,False,1)
    p=array([[x],[y],[z]])+eulermat(φ,θ,ψ)@array([[0],[1],[0]])
    ax.scatter(*p,color='red',s=3)

def draw(ax,x,r,col):
    c1,c2,φ,θ,ψ,dφ,dθ,dψ=list(x.flatten())
    c3=r*cos(θ)
    draw_wheel3D(ax,c1,c2,c3,φ,θ,ψ,r,col)
    draw_axis3D(ax,0,0,0,eye(3,3))

def SimuRollingDisk(x,xmin,xmax,ymin,ymax,zmin,zmax):
    ax = figure3D()
    dt = 0.02
    draw(ax,x,r,"blue")
    for t in arange(0,2,dt):
        x=x+dt*array([[1],[0],[0],[0],[0],[0],[0],[0]])
        pause(0.01)
        clean3D(ax,xmin,xmax,ymin,ymax,zmin,zmax)
        draw(ax,x,r,"black")

m,g,r = 5,9.81,1
c1,c2,φ,θ,ψ,dφ,dθ,dψ= 0,0, 0,0,0,0,0,0
xmin,xmax,ymin,ymax,zmin,zmax=-2,6,-4,4,0,8
x=array([[c1],[c2],[φ],[θ],[ψ],[dφ],[dθ],[dψ]])
SimuRollingDisk(x,xmin,xmax,ymin,ymax,zmin,zmax)





pause(10)

