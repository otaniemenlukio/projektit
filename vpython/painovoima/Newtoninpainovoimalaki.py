from vpython import *
#GlowScript 3.0 VPython

# Määritelläään vakiot
gc = 6.67428*10**(-11) # gravitaatiovakio
m_earth = 5.974*10**(24)
m_moon = 7.348*10**(22) ## massa kg


r_earth = 6.378*10**(6) # Maan säde meterissä
r_moon = 1.738*10**(6)

# Kuun sijainti ja nopeus alussa
k=1 # muuta kertoimen arvoa 0..1
velocity = 970*k # m/s kun etäisyys 406700km
distance = 4.067*10**(8)

a = vector(cos(45),sin(45),0)
unit_vector = a/mag(a)
unit_vector_t =rotate(unit_vector, angle=pi/2)


position = unit_vector*distance

earth = sphere(pos=vector(0,0,0), color = color.green, radius=r_earth, make_trail = True)
moon = sphere(pos =position, color=color.blue, radius=4*r_moon, make_trail=True)
moon.m =m_moon
moon.v = unit_vector_t*velocity

dt = 1

while True:
    rate(dt*60*60*24)
    unit_vector = moon.pos / mag(moon.pos)
    f = gc*m_earth*m_moon/mag(moon.pos)**2
    moon.f = -1*unit_vector*f
    a_vec = moon.f /moon.m
    moon.v = moon.v +a_vec*dt
    moon.pos = moon.pos + moon.v*dt