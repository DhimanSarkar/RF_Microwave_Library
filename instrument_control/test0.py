import scpi
import instruments

# instrument1 = scpi.scpi('TCPIP::XXXX.XXXX.XXXX::instr0::INSTR',backend='@py(default)|@sim')
# instrument2 = instruments.E36234A('TCPIP::XXXX.XXXX.XXXX::instr0::INSTR',backend='@py(default)|@sim')
# instrument3 = instruments.keysight('TCPIP::XXXX.XXXX.XXXX::instr0::INSTR',backend='@py(default)|@sim')

# instrument1 = scpi.scpi('ASLR::INSTR',backend='@sim')
# instrument1.reset() 

# # instrument1.measure(channel='ch1|ch2', parameter='voltage|current|power', parameter_type='dc|ac')
# #y = instruments.keysight('ASRL1::INSTR',backend='@sim')

# ps1 = instruments.E36234A('TCPIP::169.254.9.132::inst0::INSTR')

# ps1.reset()

# ch1_dcv_meas = ps1.measure(channel='2',parameter='V',type='dc')
# print(ch1_dcv_meas)

# inst0 = scpi.scpi('TCPIP:10.10.10.2::instr0:INSTR')

# import pyvisa
# rm = pyvisa.ResourceManager('@py')
# inst0 = rm.open_resource("TCPIP::10.10.10.2::9001::SOCKET")
# # inst0.timeout = 5000
# # inst0.read_bytes(1000, break_on_termchar='\r\n')
# inst0.read_termination = '\r\n'
# inst0.write_termination = '\r\n'
# id = inst0.query('*IDN?')
# print(str(id))

# meas = inst0.query(':CALCulate:MARKer1:Y?')
# print(str(meas))

# sa = instruments.SA_MS2720T("TCPIP::10.10.10.2::9001::SOCKET",backend='@py')
# print(sa.id)
# mea = sa.meas()
# print(mea)

sg = instruments.SG_SGS100A("TCPIP::10.10.10.1::5025::SOCKET",backend='@py')
print(sg.id)
sg.set_power()
sg.set_freq()
sg.set_pwr_level()
