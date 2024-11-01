import pyvisa
import os
import time
import re


class mtCls:    # Empty Class for testing and debugging
    def __init__(self):
        pass


class scpi():
    def __init__(self,instrumentVISA,**kwargs):
        if hasattr(self, 'backend'):
            self.backend = kwargs['backend']
        else:
            self.backend = '@py'
            
        if(self.backend == 'test'):
            print("Testing Mode!")
            print('Creating Resource Manager for ' + str(instrumentVISA) + ' ...')
            self.rm = mtCls()
            print('Establishing Instrument Connection to ' + str(instrumentVISA) + ' ...')
            self.instr = mtCls()
        else:
            print('Creating Resource Manager for ' + str(instrumentVISA) + '...')
            self.rm = pyvisa.ResourceManager(self.backend)      # Create a SCPI resource handler.
            print('Creating Instrument Connection Port for ' + str(instrumentVISA) + '...')
            self.instr = self.rm.open_resource(instrumentVISA)  # Establish communcation channel wih VISA.
                                                            #### Add basic address format verification ###
        self.instr.timeout = 25000 #msec.       # Instrument str-out read/wait time limit.    
        self.instr.chunk_size = 102400          # Data read packet size.
        self.instr.read_termination = '\n'      # Instrument str-out termination character.
        self.instr.write_termination = '\n'     # Instrument str-in termination character.
        # self.instr.query_delay = 0.1 #sec.        # Delay between two write() statements.
                                                # Ref. https://pyvisa.readthedocs.cio/en/latest/introduction/resources.html

    def __del__(self):
        self.instr.close()
        pass

    def reset(self):
        self.instr.write('*RST')
        return 0

    def get_id(self):
        self.id=self.instr.query('*IDN?')
        print(self.id)
        return 0

    def set(self,*args,**kwargs):
        self.operation = 'set'
        if 'channel' in kwargs:
            self.channel = kwargs.get('channel')
        elif len(args) >= 1:
            self.channel = args[0]
        else:
            self.channel = 1
        return self   
     
    def get(self,*args,**kwargs):
        self.operation = 'get'
        if 'channel' in kwargs:
            self.channel = kwargs.get('channel')
        elif len(args) >= 1:
            self.channel = args[0]
        else:
            self.channel = 1
        return self    

    def frequency(self,freq,*args,**kwargs):
        pass
        return self

    def voltage(self,*args,**kwargs):
        pass
        return self
    
    def current(self,*args,**kwargs):
        pass

    def power(self,*args,**kwargs):
        pass
        return self