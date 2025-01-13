import scpi
import time

####################################################
#####   Power Supply         #######################
#####   Keysight - E36234A   #######################
####################################################
class PS_E36234A(scpi.scpi):
    def __init__(self,instrumentVISA):
        super().__init__(instrumentVISA)
        self.instr_type = 'Power Supply'
        self.id = self.instr.query('*IDN?')
        print("Connection Successful with " + str(self.id))

    def __del__(self):
        super().__del__()
    
    def voltage(self, *args, **kwargs):
        if hasattr(self, 'channel') != True:
            print("Channel not defined!")
            return 0
        else:
            pass

        if self.operation == 'set':
            # SCPI Syntax-> [SOURce:]VOLTage[:LEVel][:IMMediate][:AMPLitude]<SPACE>{<voltage>|MINimum|MAXimum|UP|DOWN|DEFault}<SPACE>(@chanlist)
            voltage = args[0]
            self.voltage_status = voltage
            scpi_statement = ':SOURce:VOLTage:LEVel:IMMediate:AMPLitude ' + str(voltage) + ',(@' + str(self.channel) + ')'
            self.instr.write(scpi_statement)
        elif self.operation == 'get':
            # SCPI Syntax-> MEASure[:SCALar]:VOLTage[:DC]?<SPACE>{CH1|CH2}
            scpi_statement = 'MEASure:SCALar:VOLTage:DC? CH'  +   str(self.channel)
            now_voltage = self.instr.query(scpi_statement)
            self.power_status = now_voltage
            return now_voltage
        else:
            pass
        return self
    
    def current(self, *args, **kwargs):
        if hasattr(self, 'channel') != True:
            print("Channel not defined!")
            return 0
        else:
            pass

        if self.operation == 'set':
            # SCPI Syntax-> [SOURce:]CURRent[:LEVel][:IMMediate][:AMPLitude]<SPACE>{<voltage>|MINimum|MAXimum|UP|DOWN|DEFault}<SPACE>(@chanlist)
            voltage = args[0]
            self.voltage_status = voltage
            scpi_statement = ':SOURce:CURRent:LEVel:IMMediate:AMPLitude ' + str(voltage) + ',(@' + str(self.channel) + ')'
            self.instr.write(scpi_statement)
        elif self.operation == 'get':
            # SCPI Syntax-> MEASure[:SCALar]:CURRent[:DC]?<SPACE>{CH1|CH2}
            scpi_statement = 'MEASure:SCALar:CURRent:DC? CH'  +   str(self.channel)
            now_voltage = self.instr.query(scpi_statement)
            self.power_status = now_voltage
            return now_voltage
        else:
            pass
        return self
    
    def state(self,*args,**kwargs):
        if hasattr(self, 'channel') != True:
            print("Channel not defined!")
            return 0
        else:
            pass

        # SCPI SYNTAX-> OUTPut[:STATe]<SPACE>{OFF|ON|0|1}<SPACE>(@{1|2}})
        if self.operation == 'set':
            stat = args[0]
            scpi_statement = 'OUTPut:STATe ' + str(stat) + ',(@' + str(self.channel) + ')'
            self.instr.write(scpi_statement)
            self.status = stat
        elif self.operation == 'get':
            scpi_statement = 'OUTPut:STATe? ' + '(@' + str(self.channel) + ')'
            now_state = self.instr.query(scpi_statement)
            self.status = now_state
            return now_state
        else:
            pass
        return self

    @property
    def enable(self,*args,**kwargs):
        self.state(1)
    @property
    def disable(self,*args,**kwargs):
        self.state(0)



####################################################
#####   Power Sensor         #######################
#####   Keysight - U8488A    #######################
####################################################
class PM_U8488A(scpi.scpi):
    def __init__(self,instrumentVISA):
        super().__init__(instrumentVISA)
        self.instr_type = 'Power Sensor'
        self.id = self.instr.query('*IDN?')
        print("Connection Successful with " + str(self.id))
        
    def __del__(self):
        super().__del__()

    def power(self, *args, **kwargs):
        if self.operation == 'set':
            print(' \'set()\' Operation Not Allowed!')
        elif self.operation == 'get':
            scpi_statement = ':READ:SCALar:POWer:AC?' # FETCh -> fastest READ -> moderate with configuratble data aquisition MEASure -> most accurate not configurable
            now_pwr = self.instr.query(scpi_statement)
            self.power_status = now_pwr
            return now_pwr
        else:
            pass
        return self
    
    def unit(self, *args, **kwargs):
        if self.operation == 'set':
            print(' \'set()\' Operation Not Allowed!')
        elif self.operation == 'get':
            scpi_statement = ':UNIT:POWer?'
            now_pwr_unit = self.instr.query(scpi_statement)
            self.power_unit = now_pwr_unit
            return now_pwr_unit
        else:
            pass
        return self
    
    def config(self, *args, **kwargs):
        if self.operation == 'set':
            if 'average' in kwargs: 
                scpi_statement = 'SENSe:AVERage:COUNt ' + str(kwargs['average'])
                self.instr.write(scpi_statement)
            else:
                print("No configuration attributes defined!")
        elif self.operation == 'get':
            pass
        else:
            pass
        return self




####################################################
#####   Spectrum Analyzer   ########################
#####   Anritsu - MS2720T   ########################
####################################################
class SA_MS2720T(scpi.scpi):
    def __init__(self,instrumentVISA,**kwargs):
        super().__init__(instrumentVISA,backend='@py')
        self.instr_type = 'Spectrum Analyzer'
        self.instr.read_termination = '\n'    # Specific termination character for Anritsu MS2720T
        self.instr.write_termination = '\n'   # Specific termination character for Anritsu MS2720T
        self.id = self.instr.query('*IDN?')
        print("Connection Successful with " + str(self.id))

    def __del__(self):
        super().__del__()

    def meas(self):
        measOut = self.instr.query(':CALCulate:MARKer1:Y?')
        return measOut

    def marker(self, *args, **kwargs):
        if self.operation == 'set':
            marker_number = args[0]
            marker_freq = args[1]
            scpi_statement = ':CALCulate:MARKer' + str(marker_number) + ':X ' + str(marker_freq)
            self.instr.write(scpi_statement)
        elif self.operation == 'get':
            if len(args) >= 1:
                markerNum = args[0]
            else:
                markerNum = 1

            scpi_statement_01 = ':INITiate:IMMediate AVERage'   # Initiate a new average sweep
            scpi_statement_02 = ':SENSe:SWEep:TIME:ACTual?'     # Get Sweep Time
            scpi_statement_03 = ':STATus:OPERation?'            # Get sweep status -> 256|0 if sweep complete|incomplete
            scpi_statement_1 = ':CALCulate:MARKer' + str(markerNum) + ':X?' # Get Marker Frequency
            scpi_statement_2 = ':CALCulate:MARKer' + str(markerNum) + ':Y?' # Get Marker Power

            single_sweep_time = self.instr.query(scpi_statement_02) # Get Sweep Time
            self.instr.write(scpi_statement_01)                     # Initiate a new average sweep
            while int(self.instr.query(scpi_statement_03)) != 256:
                # time.sleep(single_sweep_time)                     # Wait for (atleast) single sweep time
                time.sleep(1)     # Wait for 1s
            
            now_marker = [self.instr.query(scpi_statement_1),self.instr.query(scpi_statement_2)]
            self.marker_status = now_marker
            return now_marker
        else:
            pass
        return self

    def frequency(self, *args, **kwargs):
        if self.operation == 'set':
            center_frequency = args[0]
            # SCPI syntax -> [:SENSe]:FREQuency:CENTer <freq>
            scpi_statement = ':SENSe:FREQuency:CENTer ' + str(center_frequency)
            self.instr.write(scpi_statement)
        elif self.operation == 'get':
            # SCPI syntax -> [:SENSe]:FREQuency:CENTer?
            scpi_statement = ':SENSe:FREQuency:CENTer?'
            center_frequency = self.instr.query(scpi_statement)
            return center_frequency
        return self

    


####################################################
#####   Signal Generator   #########################
#####   Rhode & Schwardz - SGS100A   ###############
####################################################
class SG_SGS100A(scpi.scpi):
    def __init__(self,instrumentVISA,**kwargs):
        super().__init__(instrumentVISA,backend='@py')
        self.instr_type = 'Signal Generator'
        self.instr.read_termination = '\n'    # Specific termination character for R&S SGS100A
        self.instr.write_termination = '\n'   # Specific termination character for R&S SGS100A
        self.id = self.instr.query('*IDN?')
        print("Connection Successful with " + str(self.id))
        self.power_status = False
        self.frequency_status = False
        self.status = False
        self.channel = 1        # Set to 1 explicitly since the instrument is single channel.

    def __del__(self):
        super().__del__()
   
    
    def frequency(self, *args, **kwargs):
        if hasattr(self, 'channel') != True:
            print("Channel not defined!")
            return 0
        else:
            pass
        
        if self.operation == 'set':
            freq = args[0]
            self.frequency_status = freq
            scpi_statement = ':SOURce:FREQuency:CW ' + str(freq)
            self.instr.write(scpi_statement)
        elif self.operation == 'get':
            scpi_statement = ':SOURce:FREQuency:CW?'
            now_freq = self.instr.query(scpi_statement)
            self.frequency_status = now_freq
            return now_freq
        else:
            pass
        return self

    def power(self, *args, **kwargs):
        if hasattr(self, 'channel') != True:
            print("Channel not defined!")
            return 0
        else:
            pass

        if self.operation == 'set':
            pwr = args[0]
            self.power_status = pwr
            scpi_statement = ':SOURce:POWer:LEVel ' + str(pwr)
            self.instr.write(scpi_statement)
        elif self.operation == 'get':
            scpi_statement = ':SOURce:POWer:LEVel?'
            now_pwr = self.instr.query(scpi_statement)
            self.power_status = now_pwr
            return now_pwr
        else:
            pass
        return self
    
    def state(self,*args,**kwargs):
        if hasattr(self, 'channel') != True:
            print("Channel not defined!")
            return 0
        else:
            pass
        
        if self.operation == 'set':
            stat = args[0]
            scpi_statement = ':OUTput:STATe ' + str(stat)
            self.instr.write(scpi_statement)
            self.status = stat
        elif self.operation == 'get':
            scpi_statement = ':OUTput:STATe?'
            now_state = self.instr.query(scpi_statement)
            self.status = now_state
            return now_state
        else:
            pass
        return self

    @property
    def enable(self,*args,**kwargs):
        self.operation = 'set'
        self.state(1)
        self.operation = False
    @property
    def disable(self,*args,**kwargs):
        self.operation = 'set'
        self.state(0)
        self.operation = False