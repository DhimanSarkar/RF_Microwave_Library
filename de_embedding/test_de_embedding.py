import matplotlib.pyplot
import de_embedding_algorithms
import numpy
import skrf
import matplotlib


# s_thru_meas = [[numpy.complex128(-0.22576-0.14387j), numpy.complex128(0.48758-0.81555j)], [numpy.complex128(0.48758-0.81555j), numpy.complex128(-0.22576-0.14387j)]]
# s_line_meas = [[numpy.complex128(0.10827+0.13325j), numpy.complex128(0.76582-0.61971j)], [numpy.complex128(0.76582-0.61971j), numpy.complex128(0.10827+0.13325j)]]
# s_refl_meas = [[numpy.complex128(-0.80925+0.58747j), 0], [0, numpy.complex128(-0.80925+0.58747j)]]

# de_embedding_algorithms.TRL().reveyrandTRL(s_thru_meas,s_line_meas,s_refl_meas)


thru = skrf.Network(r'.\de_embedding\cal_std\thru.s2p')
refl = skrf.Network(r'.\de_embedding\cal_std\shrt.s1p')
line = skrf.Network(r'.\de_embedding\cal_std\line.s2p')
S = None

f_points = thru.frequency.npoints
f_list   = thru.frequency

for _i in range(0, f_points):
    s_thru_meas = thru.s[_i]
    s_line_meas = line.s[_i]
    s_refl_meas = [[refl.s[_i][0][0], 0], [0, refl.s[_i][0][0]]]

    _S = de_embedding_algorithms.TRL().reveyrandTRL(s_thru_meas,s_line_meas,s_refl_meas)
    
    if(_i == 0):
        S = numpy.array([_S])
    else:
        S = numpy.append(S, [_S], axis=0)



fixture = skrf.network.Network(s=S, frequency=f_list, z0=50)

# thru.plot_s_smith()
# refl.plot_s_smith()
# line.plot_s_smith()
fixture.plot_s_db()

matplotlib.pyplot.show()