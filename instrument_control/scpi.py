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
        self.rm = pyvisa.ResourceManager(self.backend)
        self.instr = self.rm.open_resource(instrumentVISA)
        self.instr.timeout = 25000 #msec.       # Instrument str-out read/wait time limit.    
        self.instr.chunk_size = 102400          # Data read packet size.
        self.instr.read_termination = '\r'      # Instrument str-out termination character.
        self.instr.query_delay = 2 #sec.        # Delay between two write() statements.
        self.instr.send_end = True              # Send EOI character after each write() statement.
                                                # Ref. https://pyvisa.readthedocs.cio/en/latest/introduction/resources.html

    def __del__(self):
        pass

    def reset(self):
        self.instr.write('*RST')
        return 0


    def measure(self,*args,**kwargs):
        # Setting Measurement Channel
        if(re.search(r'(?i)(CH)?(channel)?1$',kwargs['channel'])):
            channel = 1
        elif(re.search(r'(?i)(CH)?(channel)?2$',kwargs['channel'])):
            channel = 2
        else:
            channel = 1

        #Setting Measurement Parameter
        if(re.search(r'(?i)^(Voltage)?(V)?(volt)?$',kwargs['parameter'])):
            parameter = 'v'
        elif(re.search(r'(?i)^(Current)?(I)?(amp)?$',kwargs['parameter'])):
            parameter = 'i'
        elif(re.search(r'(?i)^(Power)?(P)?(watt)?$',kwargs['parameter'])):
            parameter = 'p'
        else:
            parameter = 'v'
        
        #Setting Parameter Type
        if(re.search(r'(?i)^(DC)$',kwargs['type'])):
            parameter_type = 'dc'
        elif(re.search(r'(?i)^(AC)$',kwargs['type'])):
            parameter_type = 'ac'
        else:
            parameter_type = False
        
        meas_query = 'MEASure:SCALar' +\
                        ':CURRent'*(parameter=='i') +\
                        ':VOLTage'*(parameter=='v') +\
                        ':POWer'*(parameter=='p') +\
                        ':DC'*(parameter_type=='dc') +\
                        ':AC'*(parameter_type=='ac') +\
                        '? ' +\
                        'CH' + str(channel)

        meas_data = self.instr.query(meas_query)

        return meas_data