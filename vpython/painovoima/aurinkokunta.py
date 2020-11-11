from vpython import *
#GlowScript 3.0 VPython

gc = 6.67428*10**(-11) # gravitaatiovakio

m_sun = 1.989e30 
m_earth = 5.974*10**(24)

r_earth = 6.378*10**(6) # Maan säde meterissä
v_earth =107200/3.6

AU = 149597871000 # etäisyys m

#Merkurius
m_merkurius = 330.104*10**21
v_merkurius = 47870
r_merkurius =0.39*AU

#Venus
m_venus = 6.39*10**23
v_venus = 35020
r_venus =0.7*AU

class Body():
    def __init__(self, m,  r, v):
        self.m = m
        self.r = r
        if mag(r) !=0:
            unit_n = r/mag(r)
            unit_t =rotate(unit_n, angle=pi/2)
            self.v = unit_t*v
        else:
            self.v = vector(0,0,0)
        self.a = 0
        self.new_r = r
        
        if mag(r) == 0:
            self.s = sphere (pos = r, color = color.yellow, radius = (1 * m ** (1/3)), make_trail=True)
        else:
            self.s = sphere (pos = r, color = color.red, radius = (50 * m ** (1/3)), make_trail=True)
        
        
    def act(self, force, dt):
        self.a = force / self.m
        
        self.v += self.a * dt
        
        self.new_r = self.r + self.v * dt
        
    def update(self):
        self.r = self.new_r
        self.s.pos = self.r
        
        
body_list = [Body(m_sun, vector(0, 0, 0), 0), \
            Body(m_earth, vector(0,AU,0), v_earth),\
            Body(m_merkurius, vector(r_merkurius*cos(45),r_merkurius*sin(45),0), v_merkurius),\
            Body(m_venus, vector(-r_venus*cos(45),-r_venus*sin(45),0), v_venus)]

total_time = 0

#RATE = 1000

dt = 60

RATE = dt*60*24*365

while True:
    rate(RATE)
    for i, body in enumerate(body_list):
        for j, target in enumerate(body_list):
            if body == target:
                continue
            fg_mag = gc * (target.m * body.m) / (mag(target.r - body.r) ** 2)
            dir = (target.r - body.r) / mag(target.r - body.r)
            fg = fg_mag * dir
            body.act(fg, dt)

            
            #fe_mag = -E * (target.q * body.q) / (mag(target.p - body.p) ** 2)
            #fe = fe_mag * dir
            #body.act(fe, dt)
    for body in body_list:
        body.update()
    total_time+=dt