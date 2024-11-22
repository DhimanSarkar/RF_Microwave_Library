import matplotlib.pyplot
import numpy
import scipy
import matplotlib
import matplotlib.pyplot as plt
import skrf

class network():

    def __init__(self):
        pass

    def __del__(self):
        pass

    def s_matrix(self):
        pass

class test():
    def __init__(self,path,*args,**kwargs):
        self.path = path
        # self.network = skrf.Network(str(self.path) + '\\THRU.s2p')

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
            s_fxtr[i] = [[s11_fxtr, s12_fxtr],[s21_fxtr,s22_fxtr]]
        pass
        fxtr = skrf.Network(frequency=f_list, s=s_fxtr, z0=50)

        fxtr.write_touchstone(filename='fixture_TestPort_DUTPort.s2p', dir=self.path, form='db', skrf_comment=False)

        # Debug Purpose
        fxtr.plot_s_db()
        plt.show()

    
    def ChoBurk(self): # Ref. [2]
        print("Under development! Not to rely on the resutls.")

        f_points = self.network.frequency.npoints
        f_list   = self.network.frequency

        thruS   = skrf.Network(str(self.path) + '\\THRU.s2p')
        openS   = skrf.Network(str(self.path) + '\\OPEN.s1p')
        shrt1S  = skrf.Network(str(self.path) + '\\SHRT1.s1p')
        shrt2S  = skrf.Network(str(self.path) + '\\SHRT2.s1p')

        thruY   = thruS.y
        openY   = openS.y
        shrt1Y  = shrt1S.y
        shrt2Y  = shrt2S.y

        thruZ   = thruS.z
        openZ   = openS.z
        shrt1Z  = shrt1S.z
        shrt2Z  = shrt2S.z

        g1  = 1 #openY[:,0,0]+thruY[:,0,0]
        z1  = 2 #0.5 * (1/thruY[:,0,1] + 1/shrt1Y[:,0,0] - 1/shrt2S[:,0,0])
        z3  = 3 #0.5 * (-1/thruY[:,0,1] + 1/shrt1Y[:,0,0] + 1/shrt2S[:,0,0])

        line = skrf.media.DefinedGammaZ0(frequency=f_list)
        port1 = skrf.Circuit.Port(frequency=f_list, name='port1', z0=50)
        port2 = skrf.Circuit.Port(frequency=f_list, name='port2', z0=50)
        G1 = line.resistor(1/g1, name='G1')
        Z1 = line.resistor(z1, name='Z1')
        Z3 = line.resistor(z3, name='Z3')

        netlist = [
            [(port1,0),(G1,0),(Z1,0)],
            [(port1,0),(G1,1)],
            [(Z1,1),(port2,0)],
            [(Z3,1),(port2,0)]
            ]
        fixture_circuit = skrf.Circuit(netlist)
        fixture_circuit.plot_graph(network_labels=True, port_labels=True, edge_labels=True)
        plt.show()

    
    def GlennCletusTRL(self,*args,**kwargs):    # GlennCletusTRL(thru='location\file.s2p', refl='location\file.s1p', line='location\file.s2p')
        std_thru = skrf.Network(str(kwargs['thru']))
        std_refl = skrf.Network(str(kwargs['refl']))
        std_line = skrf.Network(str(kwargs['line']))
        refl_s11 = numpy.complex128(-1+0j)

        f_points = std_thru.frequency.npoints
        # print(f_points)

        for f_index in range(0,f_points):
            # print(f_index)
            # print(std_thru.s[f_index])

            # print((std_line[f_index].t)[0])

            LT = numpy.linalg.matmul((std_line[f_index].t)[0], numpy.linalg.inv(std_thru[f_index].t)[0])  # Ref. (24) of [3]
            # check = numpy.linalg.det(LT)
            # print(numpy.abs(check))

            quadratic_coeff = [LT[1,0], (LT[1,1]-LT[0,0]), LT[0,1]]     # Ref. (30, 31) of [3]
            # print(quadratic_coeff)
            roots = numpy.roots(quadratic_coeff)
            # print(roots)

            # PATH 1
            for _i in range(0,2):
                s = roots[_i%2]
                q = roots[(_i+1) %2]

                # print((std_refl[f_index].s[0][0][0]))
                r = (q - (std_refl[f_index].s[0][0][0])) / (refl_s11 * ((std_refl[f_index].s[0][0][0]) - s))
                # print(r)

                root_choice_check = numpy.abs((LT[0][0] * q + LT[0][1]) / (LT[0][0] * r * s + LT[0][1] * r))    # Ref. (57) of [3] 
                if(root_choice_check < 1):
                    break
                else:
                    continue
            
            print(root_choice_check)
        return 0
    
    def GlennCletusTSD(self,*args,**kwargs):    # GlennCletusTRL(thru='location\file.s2p', refl='location\file.s1p', line='location\file.s2p')
        std_thru = skrf.Network(str(kwargs['thru']))
        std_refl = skrf.Network(str(kwargs['refl']))
        std_line = skrf.Network(str(kwargs['line']))
        refl_s11 = numpy.complex128(-1+0j)


        # print((std_thru.t)[1])
        # print((std_thru.s)[1])

        f_list = std_thru.frequency
        f_points = std_thru.frequency.npoints
        # print(f_points)

        for f_index in range(0,f_points):
            TX = numpy.linalg.matmul((std_line[f_index].t)[0], numpy.linalg.inv(std_thru[f_index].t)[0])  # Ref. (24) of [3]
            
            quadratic_coeff = [TX[1,0], (TX[1,1]-TX[0,0]), -TX[0,1]]     # Ref. (30, 31) of [3]
            roots = numpy.roots(quadratic_coeff)

            for _i in range(0,2):
                a = roots[_i%2]
                b = roots[(_i+1) %2]
                c = ((a * std_refl.s[f_index][0] -1) / (refl_s11 * (1 - b * std_refl.s[f_index][0])))[0]

                # _root_check = numpy.abs((TX[1][0] * b + TX[1][1]) / (TX[0][1] * (1/a) + TX[0][0]))
                # print(_root_check)
                # print(abs(a*c) > 1)

                if(abs(a*c) > 1):
                    break
                else:
                    continue

            TA_scaling = numpy.sqrt(1/(a*c - b*c))

            if(f_index == 0):
                T_A = numpy.array([[[a * TA_scaling, b*c*TA_scaling],[1*TA_scaling, c*TA_scaling]]])
            else:
                T_A = numpy.append(T_A, [[[a * TA_scaling, b*c*TA_scaling],[1*TA_scaling, c*TA_scaling]]], axis=0)
        
        T_B = numpy.linalg.matmul(numpy.linalg.inv(T_A), std_thru.t)
        
        fixture_A = skrf.network.Network(s=skrf.network.t2s(T_A), frequency=f_list, z0=50)
        fixture_B = skrf.network.Network(s=skrf.network.t2s(T_B), frequency=f_list, z0=50)

        # fixture_A.plot_s_smith()
        # fixture_B.plot_s_db()
        # plt.show()

        fixture_A.write_touchstone(filename='A.s2p', dir=r'C:\Users\GEECI\Desktop', form='db', skrf_comment=False)
        return 0

        
net1 = test(path='')
net1.GlennCletusTSD(thru=r'.\de_embedding\cal_std\thru.s2p', refl=r'.\de_embedding\cal_std\shrt.s1p', line=r'.\de_embedding\cal_std\line.s2p')



####################################################################
#   References
#   [1] T. E. Kolding, “On-wafer calibration techniques for giga-hertz CMOS measurements,” ICMTS 1999. 
#       Proceedings of 1999 International Conference on Microelectronic Test Structures (Cat. No.99CH36307), vol. 1. IEEE, pp. 105–110. 
#       DOI: 10.1109/ICMTS.1999.766225
#   [2] Vandamme, E. P., et al. “Improved Three-step De-embedding Method to Accurately Account for the Influence of Pad Parasitics in Silicon On-wafer RF Test-structures.” 
#       IEEE Transactions on Electron Devices, vol. 48, no. 4, Apr. 2001, pp. 737–42. 
#       DOI: 10.1109/16.915712.
#   [3] Engen, G. F., and C. A. Hoer. “Thru-Reflect-Line: An Improved Technique for Calibrating the Dual Six-Port Automatic Network Analyzer.” 
#       IEEE Transactions on Microwave Theory and Techniques, vol. 27, no. 12, Dec. 1979, pp. 987–93. 
#       DOI: 10.1109/tmtt.1979.1129778.
####################################################################