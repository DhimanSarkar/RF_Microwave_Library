import pyvisa
import os
import time
import re

class scpi():
    def __init__(self,instrumentVISA,**kwargs):
        try:
            self.backend = kwargs['backend']
        except KeyError:
            self.backend = '@py'
        self.rm = pyvisa.ResourceManager(self.backend)      # Create a SCPI resource handler.
        self.instr = self.rm.open_resource(instrumentVISA)  # Establish communcation channel wih VISA.
                                                            #### Add basic address format verification ###
        self.instr.timeout = 25000 #msec.       # Instrument str-out read/wait time limit.    
        self.instr.chunk_size = 102400          # Data read packet size.
        self.instr.read_termination = '\r'      # Instrument str-out termination character.
        self.instr.query_delay = 2 #sec.        # Delay between two write() statements.
        #self.instr.send_end = True             # Send EOI character after each write() statement.
                                                # Ref. https://pyvisa.readthedocs.cio/en/latest/introduction/resources.html

    def __del__(self):
        pass

    def reset(self):
        self.instr.write('*RST')
        return 0

    def id(self):
        self.id=self.instr.query('*IDN?')
        print(str(self.id))
        return str(id)