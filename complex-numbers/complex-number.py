cn1 = complex(2,3)
print(cn1)
print(cn1.real)
print(cn1.imag)
cn2 = complex(1,4)
print(cn2+cn1)

import cmath
cn = complex(2,4)
#length of a complex number. 
print("Length of a complex number: ", abs(cn))
# gets angle. return in radians, between  [-π, π]
print("Complex number Angle: ",cmath.phase(cn) )


