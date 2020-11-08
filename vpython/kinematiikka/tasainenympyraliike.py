from vpython import *
#GlowScript 3.0 VPython

# Alkuarvot

k= 0.116
m = 1200 # kg
speed = 18 #km/h
r = 22
g=9.81
velocity = vector(0, 1,0)*speed/3.6


# Luodaan objekti
ball = sphere (pos = vector(1,0,0)*r, color = color.red, radius = 0.06, make_trail=True)
ball.v = velocity



time = 0
dt = 0.001 # jos rate(1000), niin dt on käänteisluku 0.001
total_time = 0

while total_time < 100:
    rate(1000) # toista silmukka max 1000 -kertaa sekunnissa
    force = k*m*g*(vector(-ball.pos.x,-ball.pos.y,0)/mag(ball.pos))
    acc = force/m
    ball.v = ball.v + acc*dt
    ball.pos = ball.pos + ball.v*dt
    total_time = total_time + dt
    
