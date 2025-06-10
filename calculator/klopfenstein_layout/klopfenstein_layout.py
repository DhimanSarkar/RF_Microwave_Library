import ezdxf
import matplotlib.pyplot
import numpy 
import scipy
import scipy.optimize
import skrf
import matplotlib
from skrf.media import MLine


# import impedance_matching

doc = ezdxf.new(dxfversion='AC1032', setup=False, units=6)
msp = doc.modelspace()
msp.add_line((0, 0), (1, 0), dxfattribs={"layer": "MyLayer"})
doc.saveas('./calculator/klopfenstein_layout/test.dxf')



def klopfenstein(Z_high,Z_low,N,gamma_max,L):       # N-> Number of segments (ideally infinite)
                                                    # gamma_max-> minimum reflection coefficient
                                                    # L-> total length of tapering
        gamma0 = (Z_high-Z_low)/(Z_high+Z_low)                                                                              # Ref. (5.77) in [1]
        A = numpy.arccosh(gamma0/gamma_max)                                                                                 # Ref. (5.78) in [1]
        phi_integrand = lambda x: scipy.special.i1(A * numpy.sqrt(1-x**2)) / (A * numpy.sqrt(1-x**2))                       # Ref. (5.75) in [1]
        phi = lambda x: scipy.integrate.quad(phi_integrand , 0 , x)[0]                                                      # Ref. (5.75) in [1]
        Z = lambda z: numpy.exp(0.5*numpy.log(Z_low*Z_high) + gamma0/numpy.cosh(A) * numpy.power(A,2) * phi(2*z/L - 1))     # Ref. (5.74) in [1]
        ele_len_min = A/numpy.pi * 180  # Minimum electrical length of the tapering in degrees

        x = numpy.linspace(0,L,N)   # Sample point in the tapering interval
        y= numpy.array([])          # Impedance values in each samples of 'x' (initializaiton)
        for i in range(0,N):
            y = numpy.append(y,Z(x[i]))

        return [x,y,ele_len_min]    # Returns the position and impedance pair as matrix rows.




def get_w(z0):
    def cost_func(x):
        mlin = MLine(frequency=None,
            w=x, h=1.6, t=None, ep_r=2.2, mu_r=1.0, 
            rho=1.68e-08, tand=0.0009, rough=1.5e-07, 
            z0_port=None, 
            z0_override=None, 
            z0=None, 
            model='hammerstadjensen', disp='kirschningjansen', diel='djordjevicsvensson', 
            f_low=1000.0, f_high=1000000000000.0, f_epr_tand=1000000000.0, compatibility_mode=None)
        
        DUT = mlin.resistor(z0)
        return(numpy.abs(numpy.max(DUT.z0)-z0))

    res = scipy.optimize.minimize(cost_func, 1, tol=1e-6, bounds=[(0.5,30)])
    return(res.x)

print(get_w(30))     





####################################################################
#   References
#   [1] D. Pozar, Microwave Engineering. John Wiley & Sons, 2011.