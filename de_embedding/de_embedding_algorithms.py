import numpy as np
import scipy as sp
import matplotlib as mtplt
import matplotlib.pyplot as plt
import skrf as rf

class network():

    def __init__(self):
        pass

    def __del__(self):
        pass

    def s_matrix(self):
        pass

class test():
    def __init__(self,path):
        self.path = path
        self.network = rf.Network(str(self.path) + '\\THRU.s2p')

    def __del__(self):
        pass

    def test0(self):    
        f_points = self.network.frequency.npoints
        f_list   = self.network.frequency
        s_fxtr = np.zeros([f_points,2,2],dtype=np.complex128)
        for i in range(0,f_points):
            s11_thru = self.network.s[i][0][0]
            s12_thru = self.network.s[i][0][1]
            s21_thru = self.network.s[i][1][0]
            s22_thru = self.network.s[i][1][1]

            s11_fxtr = (s11_thru + s22_thru)/(2 + s12_thru + s21_thru)              # Ref. (5) in [1]
            s12_fxtr = np.sqrt(0.5 * (s12_thru + s21_thru) * (1 - s11_fxtr**2))     # Ref. (6) in [1]
            s21_fxtr = s12_fxtr
            s22_fxtr = s11_fxtr
            s_fxtr[i]   = [[s11_fxtr, s12_fxtr],[s21_fxtr,s22_fxtr]]
        pass
        fxtr = rf.Network(frequency=f_list, s=s_fxtr, z0=50)

        fxtr.write_touchstone(filename='fixture_in_DUT.s2p', dir=self.path, form='db', skrf_comment=False)

        # Debug Purpose
        fxtr.plot_s_db()
        plt.show()



####################################################################
#   References
#   [1] T. E. Kolding, “On-wafer calibration techniques for giga-hertz CMOS measurements,” ICMTS 1999. 
#       Proceedings of 1999 International Conference on Microelectronic Test Structures (Cat. No.99CH36307), vol. 1. IEEE, pp. 105–110. 
#       DOI: 10.1109/ICMTS.1999.766225
####################################################################