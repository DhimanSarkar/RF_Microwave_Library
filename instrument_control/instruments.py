import scpi


class keysight(scpi.scpi):
    def __init__(self,instrumentVISA,**kwargs):
        try:
            self.backend = kwargs['backend']
        except KeyError:
            self.backend = '@py'
        super().__init__(instrumentVISA,backend=self.backend)
    def __del__(self):
        super().__del__()

class E36234A(keysight):
    def __init__(self,instrumentVISA):
        super().__init__(instrumentVISA)
        self.instr_type = 'Power Supply'
    def __del__(self):
        super().__del__()


class SA_MS2720T(scpi.scpi):
    def __init__(self,instrumentVISA,**kwargs):
        super().__init__(instrumentVISA,backend='@py')
        self.instr.read_termination = '\r\n'    # Specific termination character for Anritsu MS2720T
        self.instr.write_termination = '\r\n'   # Specific termination character for Anritsu MS2720T
        self.id = self.instr.query('*IDN?')

    def __del__(self):
        super().__del__()

    def meas(self):
        measOut = self.instr.query(':CALCulate:MARKer1:Y?')
        return measOut
    
class SG_SGS100A(scpi.scpi):
    def __init__(self,instrumentVISA,**kwargs):
        super().__init__(instrumentVISA,backend='@py')
        self.instr.read_termination = '\r\n'    # Specific termination character for R&S SGS100A
        self.instr.write_termination = '\r\n'   # Specific termination character for R&S SGS100A
        self.id = self.instr.query('*IDN?')

    def __del__(self):
        super().__del__()

    def set_power(self):
        self.instr.write(':OUTput:STATe OFF')
        return 0
    
    def set_freq(self):
        self.instr.write(':SOURce:FREQuency:CW 1 GHz')
        return 0
    
    def set_pwr_level(self):
        self.instr.write(':SOURce:POWer:LEVel -25 dBm')
        return 0