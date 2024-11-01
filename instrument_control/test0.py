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

# sg = instruments.SG_SGS100A("TCPIP::10.10.10.1::5025::SOCKET",backend='@py')
# print(sg.id)
# sg.set_power()
# sg.set_freq()
# sg.set_pwr_level()


# inst0 = scpi.scpi('demoVISA',backend='test')

# inst0.set(channel=41).frequency('1 GHz')

sg = instruments.SG_SGS100A("TCPIP::10.10.10.1::5025::SOCKET")
pm = instruments.PM_U8488A('USB0::0x2A8D::0xA718::MY62040007::0::INSTR')
ps = instruments.PS_E36234A('TCPIP::10.10.20.1::5025::SOCKET')
sa = instruments.SA_MS2720T('TCPIP::10.10.30.1::9001::SOCKET')

# sg.set().frequency('1.111 GHz').power('-20 dBm').enable
# print(sa.get().marker(1))
# sg.set().frequency('1.111 GHz').power('-25 dBm').enable
# print(sa.get().marker(1))
# sg.set().frequency('1.111 GHz').power('-10.327 dBm').enable
# print(sa.get().marker(1))
# sg.set().disable
# print(pm.get().power())
# sg.set().power(-11.11)
# print(pm.get().power())
# sg.disable

# ps.set(channel=1).voltage(2).enable
# ps.set(2).voltage(3.333).enable
# print(ps.get(1).voltage())
# print(ps.get(2).voltage())
# ps.set(1).current(1.333)
# ps.set(2).current(0.33)


# ps.set(1).disable
# ps.set(2).disable

sg.disable
# while(True):
for i in range(1,10):
    sg.set().power(-40+3*i).enable
    y = sa.get().marker(1)
    sg.disable
    print(y)