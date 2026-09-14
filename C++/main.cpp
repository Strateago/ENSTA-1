#include <iostream>
#include "vibes.h"
#include <math.h>
#include <unistd.h>

void draw_road(float r){
    vibes::clearFigure("Road");
    vibes::drawCircle(0, 0, r+2.5, "Black[#B5C7EB]");
    vibes::drawCircle(0, 0, r-2.5, "Black[#FFFFFF]");
}

void draw_robot(double r, double theta){
    vibes::drawTank(r*cos(theta), r*sin(theta), (theta+M_PI/2.) * (180./M_PI), 4, "black[white]", vibesParams("figure", "Road"));
}

void f(float x, float v, float u, float& xdot, float& vdot){
    xdot = v;
    vdot = u;
}

void euler(float dt, float xdot, float vdot, float& x, float& v){
    x = x + dt*xdot;
    v = v + dt*vdot;
}

int main(){
    int l = 100;
    float dt = 0.05, v0 = 3, u = 1, r = l/(2*M_PI), x = 0, v, xdot, vdot, theta;
    
    vibes::beginDrawing(); // initialisation de VIBes
    vibes::newFigure("Road"); // cr´eation d’une figure
    vibes::setFigureProperties("Road",
    vibesParams("x", 100, "y", 100, "width", 400, "height", 400)); // propri´et´es de la figure
    vibes::axisLimits(-20., 20., -20., 20.); // dimensions de la vue graphique
    v = v0;
    for(int i = 0; i < 100/dt; i++){
        usleep(dt * 500000.);
        draw_road(r);
        f(x, v, u, xdot, vdot);
        euler(dt, xdot, vdot, x, v);
        theta = x/r;
        draw_robot(r, theta);
    }
    vibes::endDrawing();
    return 0;
}