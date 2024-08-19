import scpi
import instruments


y = instruments.keysight('ASRL1::INSTR',backend='@sim')

y.reset()