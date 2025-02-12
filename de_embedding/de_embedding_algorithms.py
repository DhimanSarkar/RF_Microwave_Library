import matplotlib.pyplot
import numpy
import scipy
import matplotlib
import matplotlib.pyplot as plt
import skrf

class network():

    def ___(self):
        pass

    def __del__(self):
        pass

    def s_matrix(self):
        pass

    def s2t(S):     #####################
        s11 = numpy.complex128(S[0][0])
        s12 = numpy.complex128(S[0][1])
        s21 = numpy.complex128(S[1][0])
        s22 = numpy.complex128(S[1][1])

        t11 = numpy.reciprocal(s21)
        t12 = numpy.divide(-s22, s21)
        t21 = numpy.divide(s11, s21)
        t22 = numpy.divide(-numpy.subtract(numpy.multiply(s11, s22), numpy.multiply(s12, s21)), s21)
        T = [[t11, t12], [t21, t22]]

        return T
    #####################################
    
    def t2s(T):     #####################
        t11 = numpy.complex128(T[0][0])
        t12 = numpy.complex128(T[0][1])
        t21 = numpy.complex128(T[1][0])
        t22 = numpy.complex128(T[1][1])

        s11 = numpy.divide(t21, t11)
        s12 = numpy.divide(numpy.subtract(numpy.multiply(t11, t22), numpy.multiply(t12, t21)), t11)
        s21 = numpy.reciprocal(t11)
        s22 = numpy.divide(-t12, t11)
        S = [[s11, s12], [s21, s22]]

        return S
    ####################################

class TRL():
    def ___(self,*args,**kwargs):
        pass

    def __del__(self):
        pass

    def thru2x(self, thru_path, *args, **kwargs):   # 2X THRU Implementation
        if 'export_path' in kwargs:
            export_path = kwargs['export_path']
        else:
            export_path = '.\\'

        thru =  skrf.Network(thru_path)
        
        f_points = thru.frequency.npoints
        f_list   = thru.frequency

        s_fxr = numpy.zeros([f_points,2,2],dtype=numpy.complex128)

        for i in range(0,f_points):
            s11_t = numpy.complex128(thru.s[i][0][0])
            s12_t = numpy.complex128(thru.s[i][0][1])
            s21_t = numpy.complex128(thru.s[i][1][0])
            s22_t = numpy.complex128(thru.s[i][1][1])

            s11 = numpy.divide((s11_t + s22_t), (2 + s12_t + s21_t))        # Ref. (5) in [1]
            s21 = numpy.sqrt(0.5 * (s12_t + s21_t) * (1 - s11**2))          # Ref. (6) in [1]
            
            if(i == 0): # choosing the phase of the first/initial frequency
                s21_ang1 = numpy.angle(s21)
                s21_ang2 = numpy.angle(-s21)
                s21_ang_min  = numpy.minimum(numpy.abs(s21_ang1),numpy.abs(s21_ang2))
                s21_ang = s21_ang1 * (numpy.abs(s21_ang1) == s21_ang_min) + s21_ang2 * (numpy.abs(s21_ang1) != s21_ang_min)

                s21 = numpy.abs(s21) * numpy.exp(s21_ang*1j)

                # print(numpy.rad2deg(s21_ang1), end='\t')
                # print(numpy.rad2deg(s21_ang2), end='\t')
                # print(numpy.rad2deg(s21_ang), end='\n')
                # print("  ", end="\n")
                # print("  ", end="\n")

            else: # choosing the phase of the consequent frequencies in relative to previous frequency point
                s21_ang1 = numpy.angle(s21)
                s21_ang2 = numpy.angle(-s21)

                s21_prev_ang = numpy.angle(s_fxr[i-1][0][1])

                ang_delta1 = s21_prev_ang - s21_ang1
                ang_delta2 = s21_prev_ang - s21_ang2
                s21_ang_min  = numpy.minimum(numpy.abs(ang_delta1),numpy.abs(ang_delta2))
                if_ang1_min = bool (numpy.abs(ang_delta1) == s21_ang_min)
                
                if(numpy.abs(ang_delta1+ang_delta2) >= numpy.deg2rad(360)):
                    s21_ang = s21_ang1 * (not(if_ang1_min)) + s21_ang2 * ((if_ang1_min))
                else:
                    s21_ang = s21_ang1 * if_ang1_min + s21_ang2 * (not(if_ang1_min))

                s21 = numpy.abs(s21) * numpy.exp(s21_ang*1j)

                # print(numpy.rad2deg(s21_ang1), end='\t')
                # print(numpy.rad2deg(s21_ang2), end='\t')
                # print(numpy.rad2deg(s21_ang), end='\n')
                # print(numpy.rad2deg(ang_delta1), end='\t')
                # print(numpy.rad2deg(ang_delta2), end='\n')
                # print("  ", end="\n")
                # print("  ", end="\n")




            s_fxr[i] = [[s11, s21],[s21,s11]]
        pass
        
        fxr = skrf.Network(frequency=f_list, s=s_fxr, z0=50)
        fxr.write_touchstone(filename='fixture_TestPort_DUTPort.s2p', form='ma', dir=export_path, skrf_comment=False)
        return fxr.to_dataframe

    
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



    def reveyrandTRL(self,thru,refl,line,*args,**kwargs):
        # s_t_meas = [[numpy.complex128(-0.22576-0.14387j), numpy.complex128(0.48758-0.81555j)], [numpy.complex128(0.48758-0.81555j), numpy.complex128(-0.22576-0.14387j)]]
        # s_line_meas = [[numpy.complex128(0.10827+0.13325j), numpy.complex128(0.76582-0.61971j)], [numpy.complex128(0.76582-0.61971j), numpy.complex128(0.10827+0.13325j)]]
        # s_refl_meas = [[numpy.complex128(-0.80925+0.58747j), 0], [0, numpy.complex128(-0.80925+0.58747j)]]
        s_t_meas = thru
        s_line_meas = refl
        s_refl_meas = line

        

        t_t_meas = network.s2t(s_t_meas)
        t_line_meas = network.s2t(s_line_meas)

        M = numpy.matmul(numpy.linalg.inv(t_t_meas), t_line_meas)
        N = numpy.matmul(t_line_meas, numpy.linalg.inv(t_t_meas))

        M_coeff = [M[1][0], (M[0][0]-M[1][1]), -M[0][1]]
        N_coeff = [N[1][0], (N[0][0]-N[1][1]), -N[0][1]]

        M_sol = numpy.roots(M_coeff)
        N_sol = numpy.roots(N_coeff)

        M_sol_abs = list(numpy.abs(M_sol))
        M_sol_abs_max = numpy.max(numpy.abs(M_sol))
        M_max_index = M_sol_abs.index(M_sol_abs_max)
        M_min_index = numpy.mod((M_max_index + 1), 2)
        c1 = M_sol[M_max_index] # T22/T21 | abs(T22/T21) > abs(T12/T11) [output block]
        c2 = M_sol[M_min_index] # T12/T11 | abs(T12/T11) > abs(T12/T11) [output block]

        N_sol_abs = list(numpy.abs(M_sol))
        N_sol_abs_max = numpy.max(numpy.abs(M_sol))
        M_max_index = N_sol_abs.index(N_sol_abs_max)
        M_min_index = numpy.mod((M_max_index + 1), 2)
        c3 = M_sol[M_max_index] # TT22/TT21 | abs(TT22/TT21) > abs(TT12/T11) [input block]
        c4 = M_sol[M_min_index] # TT12/TT11 | abs(TT12/TT11) > abs(TT12/T11) [input block]

        c5 = numpy.divide((1 + c4 * s_t_meas[0][0]), s_t_meas[1][0])  # T11/TT11 [input block]
        c6 = numpy.divide(s_t_meas[0][1], (s_t_meas[1][1] + c1))      # T21/TT22 [input block]

        c7_num = c5 * numpy.divide((s_refl_meas[1][1] + c2), (s_refl_meas[1][1] + c1))
        c7_den = c6 * c3 * numpy.divide((1 + c3 * s_refl_meas[0][0]), (1 + c4 * s_refl_meas[0][0]))
        c7 = numpy.sqrt(numpy.divide(c7_num, c7_den))   # TT21/TT11 [output block]

        gamma_std_verify = c7 * numpy.divide((1 + c3 * s_refl_meas[0][0]), (1 + c4 * s_refl_meas[0][0]))

        if(numpy.real(gamma_std_verify) > 0):   # real(gamma) = 1 for OPEN, real(gamma) = -1 for SHRT
            c7 = -c7                            # if real(gamma) > 0 choose alternate sign of c7 for SHRT
        else:
            pass

        # IMPORTANT
        k = numpy.sqrt(numpy.reciprocal(c3 * c7 - c4 * c7))

        print(numpy.angle(k))
        # need to implement K unwrapping verification

        TT_in = numpy.multiply([[1, c4], [c7, c3*c7]], k)
        T_in = numpy.linalg.inv(TT_in)
        T_out = [[c5, c2*c5], [c6*c3*c7, c1*c6*c7]]
        S_in = network.t2s(T_in)
        S_out = network.t2s(T_out)
        
        return S_out
    

    def GlennCletusTSD(self,*args,**kwargs):    # GlennCletusTRL(thru='location\file.s2p', refl='location\file.s1p', line='location\file.s2p')
        std_t = skrf.Network(str(kwargs['thru']))
        std_refl = skrf.Network(str(kwargs['refl']))
        std_line = skrf.Network(str(kwargs['line']))
        refl_s11 = numpy.complex128(-1+0j)


        # print((std_t.t)[1])
        # print((std_t.s)[1])

        f_list = std_t.frequency
        f_points = std_t.frequency.npoints
        # print(f_points)

        for f_index in range(0,f_points):
            TX = numpy.linalg.matmul((std_line[f_index].t)[0], numpy.linalg.inv(std_t[f_index].t)[0])  # Ref. (24) of [3]
            
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
        
        T_B = numpy.linalg.matmul(numpy.linalg.inv(T_A), std_t.t)
        
        fixture_A = skrf.network.Network(s=skrf.network.t2s(T_A), frequency=f_list, z0=50)
        fixture_B = skrf.network.Network(s=skrf.network.t2s(T_B), frequency=f_list, z0=50)

        # fixture_A.plot_s_smith()
        # fixture_B.plot_s_db()
        # plt.show()

        fixture_A.write_touchstone(filename='A.s2p', dir=r'C:\Users\GEECI\Desktop', form='ma', skrf_comment=False)
        return 0
    
    def TRL(self, thru_path,refl_path,line_path, *args, **kwargs):   # TRL
        if 'export_path' in kwargs:
            export_path = kwargs['export_path']
        else:
            export_path = '.\\'

        thru =  skrf.Network(thru_path)
        refl =  skrf.Network(refl_path)
        line =  skrf.Network(line_path)
        
        f_points = thru.frequency.npoints
        f_list   = thru.frequency

        s_fxr_in = numpy.zeros([f_points,2,2],dtype=numpy.complex128)
        s_fxr_out = numpy.zeros([f_points,2,2],dtype=numpy.complex128)

        for i in range(0,f_points):
            s11_t = numpy.complex128(thru.s[i][0][0])
            s12_t = numpy.complex128(thru.s[i][0][1])
            s21_t = numpy.complex128(thru.s[i][1][0])
            s22_t = numpy.complex128(thru.s[i][1][1])
            s_t = [[s11_t, s12_t],[s21_t, s22_t]]
            t_t = network.s2t(s_t)

            s11_r = numpy.complex128(refl.s[i][0][0])
            s12_r = numpy.complex128(refl.s[i][0][1])
            s21_r = numpy.complex128(refl.s[i][1][0])
            s22_r = numpy.complex128(refl.s[i][1][1])
            s_r = [[s11_r, s12_r],[s21_r, s22_r]]

            s11_l = numpy.complex128(line.s[i][0][0])
            s12_l = numpy.complex128(line.s[i][0][1])
            s21_l = numpy.complex128(line.s[i][1][0])
            s22_l = numpy.complex128(line.s[i][1][1])
            s_l = [[s11_l, s12_l],[s21_l, s22_l]]
            t_l = network.s2t(s_l)

            M = numpy.matmul(numpy.linalg.inv(t_t), t_l)
            N = numpy.matmul(t_l, numpy.linalg.inv(t_t))

            M_coeff = [M[1][0], (M[0][0]-M[1][1]), -M[0][1]]
            N_coeff = [N[1][0], (N[0][0]-N[1][1]), -N[0][1]]

            M_sol = numpy.roots(M_coeff)
            N_sol = numpy.roots(N_coeff)

            M_sol_abs = list(numpy.abs(M_sol))
            M_sol_abs_min = numpy.min(numpy.abs(M_sol))
            M_sol_min_index = M_sol_abs.index(M_sol_abs_min)
            M_sol_max_index = numpy.mod((M_sol_min_index + 1), 2)

            c1 = M_sol[M_sol_max_index] # T22/T21 | abs(T22/T21) > abs(T12/T11) [output block]
            c2 = M_sol[M_sol_min_index] # T12/T11 | abs(T12/T11) > abs(T12/T11) [output block]

            N_sol_abs = list(numpy.abs(N_sol))
            N_sol_abs_min = numpy.min(numpy.abs(N_sol))
            N_sol_min_index = N_sol_abs.index(N_sol_abs_min)
            N_sol_max_index = numpy.mod((N_sol_min_index + 1), 2)

            c3 = N_sol[N_sol_max_index] # TT22/TT21 | abs(TT22/TT21) > abs(TT12/T11) [input block]
            c4 = N_sol[N_sol_min_index] # TT12/TT11 | abs(TT12/TT11) > abs(TT12/T11) [input block]

            c5 = numpy.divide((1 + c4 * s_t[0][0]), s_t[1][0])  # T11/TT11 [input block]
            c6 = numpy.divide(s_t[0][1], (s_t[1][1] + c1))      # T21/TT22 [input block]

            c7_num = c5 * numpy.divide((s_r[1][1] + c2), (s_r[1][1] + c1))
            c7_den = c6 * c3 * numpy.divide((1 + c3 * s_r[0][0]), (1 + c4 * s_r[0][0]))
            c7 = numpy.sqrt(numpy.divide(c7_num, c7_den))       # TT21/TT11 [input block]

            gamma_std_verify = c7 * numpy.divide((1 + c3 * s_r[0][0]), (1 + c4 * s_r[0][0]))
            # assuming REFL standard used is SHRT
            if(numpy.real(gamma_std_verify) > 0):   # real(gamma) = 1 for OPEN, real(gamma) = -1 for SHRT
                c7 = -c7                            # if real(gamma) > 0 choose alternate sign of c7 for SHRT
            else:
                pass

            # IMPORTANT
            if(i == 0): # fixing inital value of 'k' such that ang(s21) is minimum
                k = numpy.sqrt(numpy.reciprocal(c3 * c7 - c4 * c7))

                TT_in1 = numpy.multiply([[1, c4], [c7, c3*c7]], k)
                T_in1 = numpy.linalg.inv(TT_in1)
                S_in1 = network.t2s(T_in1)

                TT_in2 = numpy.multiply([[1, c4], [c7, c3*c7]], -k)
                T_in2 = numpy.linalg.inv(TT_in2)
                S_in2 = network.t2s(T_in2)

                s21_ang1 = numpy.angle(S_in1[1][0])
                s21_ang2 = numpy.angle(S_in2[1][0])
                s21_ang_min  = numpy.minimum(numpy.abs(s21_ang1),numpy.abs(s21_ang2))

                if(numpy.abs(s21_ang1) == s21_ang_min):
                    S_in = S_in1
                    T_in = T_in1
                else:
                    S_in = S_in2
                    T_in = T_in2

                s_fxr_in[i] = S_in


            else: # choosing the phase of the consequent frequencies in relative to previous frequency point
                k = numpy.sqrt(numpy.reciprocal(c3 * c7 - c4 * c7))

                TT_in1 = numpy.multiply([[1, c4], [c7, c3*c7]], k)
                T_in1 = numpy.linalg.inv(TT_in1)
                S_in1 = network.t2s(T_in1)

                TT_in2 = numpy.multiply([[1, c4], [c7, c3*c7]], -k)
                T_in2 = numpy.linalg.inv(TT_in2)
                S_in2 = network.t2s(T_in2)

                s21_ang1 = numpy.angle(S_in1[1][0])
                s21_ang2 = numpy.angle(S_in2[1][0])

                s21_prev_ang = numpy.angle(s_fxr_in[i-1][0][1])

                ang_delta1 = s21_prev_ang - s21_ang1
                ang_delta2 = s21_prev_ang - s21_ang2
                s21_ang_min  = numpy.minimum(numpy.abs(ang_delta1),numpy.abs(ang_delta2))
                if_ang1_min = bool (numpy.abs(ang_delta1) == s21_ang_min)
                
                if(numpy.abs(ang_delta1+ang_delta2) >= numpy.deg2rad(360)):
                    S_in = S_in1 * (not(if_ang1_min)) + S_in2 * ((if_ang1_min))
                else:
                    S_in = S_in1 * if_ang1_min + S_in2 * (not(if_ang1_min))

                s_fxr_in[i] = S_in
        
            t_in = network.s2t(S_in)
            t_out = numpy.matmul(numpy.linalg.inv(t_in), t_t)
            s_fxr_out[i] = network.t2s(t_out)
    

        fxr_in = skrf.Network(frequency=f_list, s=s_fxr_in, z0=50)
        fxr_in.write_touchstone(filename='fixture_TestPort_DUTPort.s2p', form='ma', dir=export_path, skrf_comment=False)
        fxr_out = skrf.Network(frequency=f_list, s=s_fxr_out, z0=50)
        fxr_out.write_touchstone(filename='fixture_DUTPort_TestPort.s2p', form='ma', dir=export_path, skrf_comment=False)
        return [fxr_in.to_dataframe, fxr_out.to_dataframe]






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