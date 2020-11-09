from vpython import *
#GlowScript 3.0 VPython

# Gravitaatiovakio
gc = 6.67384*10**(-11) 

# Maa
M_earth = 5.9736e24 #Maan massa kg
M_radius = 6.378e6 # Maan säde 

# Kuu
m_moon = 7.342e22 #kuun massa kg
m_radius = 1.74e6 # Kuun säde 
#distance = 3.844e8 # keskietäisyys maasta
distance =4.067e8 #Kuun suurin etäisyys maasta
velocity = 970 # nopeus suurimmalla etäisyydellä

# Tilastoja
#a=3.844e8 # keskietäisyys maasta
#r_p =  3.564e8 #etäisyys perihelissä, lyhin etäisyys
#r_a= 4.067e8 etäisyys apihelissä, suurin etäisyys 
#a=(r_p+r_a)/2
#velocity =sqrt(M_earth*gc*(2/distance-1/a))

moon = sphere(pos=vector(cos(45),sin(45),0)*distance, radius=4*m_radius , color=color.blue, make_trail=True )
unit_vector_n = vector(-moon.pos.x, -moon.pos.y,0)/mag(moon.pos)
unit_vector_t = rotate(unit_vector_n, angle = pi/2)
moon.m = m_moon
moon.v = velocity*unit_vector_t


earth = sphere(pos=vector(0,0,0), radius=M_radius , color=color.green,  make_trail=True)
earth.m = M_earth

time = 0
dt = 1


while True:
    rate(1*60*60*24)
    
    unit_vector_n =vector(-moon.pos.x,-moon.pos.y,0)/mag(moon.pos)
    gravity = (gc*earth.m*moon.m/distance**2)*unit_vector_n
    acc =gravity /moon.m # keskeiskiihtyvyys eli normaalikiihtyvyys a_n=v**2/r
    moon.v = moon.v +acc*dt
    moon.pos=moon.pos +moon.v*dt
   
    
    
