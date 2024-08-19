

# RF & Microwave Library

 - Design Calculators
	 - **Impedance Matching**
		 1. **Klopfenstein Tapering** 
		  
				taper1 = taper(Z1,Z2)
				[x,y,theta]=taper1.klopfenstein(num_sections,min_reflection_coeff,norm_length)
				print('position: ' + str(x))
				print('impedance: ' + str(y))
				print('min electrical length: ' + str(theta))


# Instrument Control
**Python SCPI Library**

 - Methods:
	 - `scpi('VISA_address',[optional]backend='@py(default)|@sim')`
	 - `keysight('VISA_address',[optional]backend='@py(default)|@sim')`
	 - `E36234A('VISA_address',[optional]backend='@py(default)|@sim')`
	 
	 - `measure(channel='ch1(default)|ch2', parameter='voltage(default)|current|power', parameter_type='dc(defalut)|ac')`
 - Example:

	    import  scpi
	    import  instruments
	    
	    instrument1 = scpi.scpi('TCPIP::XXXX.XXXX.XXXX::instr0::INSTR',backend='@py(default)|@sim')
	    instrument2 = instruments.E36234A('TCPIP::XXXX.XXXX.XXXX::instr0::INSTR',backend='@py(default)|@sim')
	    instrument3 = instruments.keysight('TCPIP::XXXX.XXXX.XXXX::instr0::INSTR',backend='@py(default)|@sim')
	    
	    instrument1.reset()
	    instrument1.measure(channel='ch1|ch2', parameter='voltage|current|power', parameter_type='dc|ac')

