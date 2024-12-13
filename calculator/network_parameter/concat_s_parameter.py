import matplotlib.pyplot
import skrf
import numpy
import matplotlib

nports = 4

SP12 = skrf.network.Network(r'p12.s2p')
SP13 = skrf.network.Network(r'p13.s2p')
SP14 = skrf.network.Network(r'p14.s2p')
SP32 = skrf.network.Network(r'p32.s2p')
SP42 = skrf.network.Network(r'p42.s2p')
SP34 = skrf.network.Network(r'p34.s2p')
SP12.name = 'p12'
SP13.name = 'p13'
SP14.name = 'p14'
SP32.name = 'p32'
SP42.name = 'p42'
SP34.name = 'p34'

network_list = [SP12, SP13, SP14, SP32, SP42, SP34]

S_full = skrf.network.n_twoports_2_nport(network_list, nports)
S_full.write_touchstone(filename='concat', dir=r'', form='ri', skrf_comment=False)

# S_full.plot_s_db()
# matplotlib.pyplot.show()