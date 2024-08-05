

# RF & Microwave Library

 - Design Calculators
	 - **Impedance Matching**
		 1. **Klopfenstein Tapering** 
		  
				taper1 = taper(Z1,Z2)
				[x,y,theta]=taper1.klopfenstein(num_sections,min_reflection_coeff,norm_length)
				print('position: ' + str(x))
				print('impedance: ' + str(y))
				print('min electrical length: ' + str(theta))


