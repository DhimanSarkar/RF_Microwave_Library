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