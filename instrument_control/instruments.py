import scpi


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
            scpi_statement = ':MEASure:SCALar:POWer:AC?'
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
            print(' \'set()\' Operation Not Allowed!')
        elif self.operation == 'get':
            if len(args) >= 1:
                markerNum = args[0]
            else:
                markerNum = 1
            scpi_statement_1 = ':CALCulate:MARKer' + str(markerNum) + ':X?' # Get Marker Frequency
            scpi_statement_2 = ':CALCulate:MARKer' + str(markerNum) + ':Y?' # Get Marker Power
            now_marker = [self.instr.query(scpi_statement_1),self.instr.query(scpi_statement_2)]
            self.marker_status = now_marker
            return now_marker
        else:
            pass
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
        self.state(1)
    @property
    def disable(self,*args,**kwargs):
        self.state(0)