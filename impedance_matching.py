import numpy as np
import scipy as sp
import matplotlib as mtplt
import matplotlib.pyplot as plt
import skrf as rf


class taper:
    def __init__(self,Z1,Z2):
        if(Z1>Z2):              # Implementation Convention -> Matching from low_impedance to high_impedance
            self.Z_low = Z2
            self.Z_high = Z1
            self.direction = "H2L"  # Hight to Low Impedance Transformation
        else:
            self.Z_low = Z1
            self.Z_high = Z2
            self.direction = "L2H"  # Low to Hight Impedance Transformation
        

    def klopfenstein(self,N,gamma_max,L):       # N-> Number of segments (ideally infinite)
        self.type = "klopfenstein"              # gamma_max-> maximum passband ripple
                                                # L-> total length of tapering
        gamma0 = (self.Z_high-self.Z_low)/(self.Z_high+self.Z_low)                                                      # Ref. (5.77) in [1]
        A = np.arccosh(gamma0/gamma_max)                                                                                # Ref. (5.78) in [1]
        phi_integrand = lambda x: sp.special.i1(A * np.sqrt(1-x**2)) / (A * np.sqrt(1-x**2))                            # Ref. (5.75) in [1]
        phi = lambda x: sp.integrate.quad(phi_integrand , 0 , x)[0]                                                     # Ref. (5.75) in [1]
        Z = lambda z: np.exp(0.5*np.log(self.Z_low*self.Z_high) + gamma0/np.cosh(A) * np.power(A,2) * phi(2*z/L - 1))   # # Ref. (5.74) in [1]

        x = np.linspace(0,L,N)  # Sample point in the tapering interval
        y= np.array([])         # Impedance values in each samples of 'x' (initializaiton)
        for i in range(0,N):
            y = np.append(y,Z(x[i]))
        if(self.direction == "H2L"):
            y = np.flip(y)
        else:
            pass
        return [x,y]            # Returns the position and impedance pair as matrix rows.
    


####################################################################
#   References
#   [1] D. Pozar, Microwave Engineering. John Wiley & Sons, 2011.


####################################################################
#   Examples
#
#   Klopfenstein Tapering
#   tl1 = taper(50,100)
#   [x,y]=tl1.klopfenstein(5,0.01,1)
#   print(x)
#   print(y)