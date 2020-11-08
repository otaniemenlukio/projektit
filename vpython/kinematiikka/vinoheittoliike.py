from vpython import *
#GlowScript 3.0 VPython
# Vinoheittoliike


ball = sphere (pos =vector(0,0,0), color = color.red, radius = 0.02, make_trail=True)
ball.v = vector (-2.0, 2.0, 0)
ball.a = vector(0, -9.81,0)

time = 0
dt = 0.001 # jos rate(1000), niin dt on käänteisluku 0.001

y_max = 0
v_ground = 0

while ball.pos.y >= 0:
    rate(1000) # toista silmukka max 1000 -kertaa sekunnissa
    print('x-koordinaatti: ', ball.pos.x, 'y-koordinaatti', ball.pos.y)
    ball.pos = ball.pos + ball.v*dt
    ball.v = ball.v + ball.a*dt
    if ball.pos.y > y_max:
        y_max = ball.pos.y
    if ball.pos.y <= 0:
        v_ground = (ball.v.x**2 +ball.v.y**2)**0.5
        break

print('Pallo nousi', y_max, 'korkeudelle')
print('Pallo osui maahan nopeudella', v_ground)
print('Nopeuden komponentit: v_x', ball.v.x, 'v_y:', ball.v.y)
angle = atan(ball.v.y/ball.v.x)*180/3.14
print('kulma vakatasonsuhteen:', angle ) 