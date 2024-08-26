import scpi
import instruments

# instrument1 = scpi.scpi('TCPIP::XXXX.XXXX.XXXX::instr0::INSTR',backend='@py(default)|@sim')
# instrument2 = instruments.E36234A('TCPIP::XXXX.XXXX.XXXX::instr0::INSTR',backend='@py(default)|@sim')
# instrument3 = instruments.keysight('TCPIP::XXXX.XXXX.XXXX::instr0::INSTR',backend='@py(default)|@sim')

instrument1 = scpi.scpi('ASLR::INSTR',backend='@sim')
instrument1.reset() 

# instrument1.measure(channel='ch1|ch2', parameter='voltage|current|power', parameter_type='dc|ac')
#y = instruments.keysight('ASRL1::INSTR',backend='@sim')

ps1 = instruments.E36234A('TCPIP::169.254.9.132::inst0::INSTR')

ps1.reset()

ch1_dcv_meas = ps1.measure(channel='2',parameter='V',type='dc')
print(ch1_dcv_meas)