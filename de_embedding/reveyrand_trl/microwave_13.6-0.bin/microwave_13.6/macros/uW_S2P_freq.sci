function S2=uW_S2P_freq(Sin,freqlist)

	// Spline de Sin et Sout
	frequence=freqlist;
	if size(freqlist,2)>size(freqlist,1) then,
		frequence=frequence.';
	end;
	
	// Sin
	f_Sij=Sin.frequency;
	for k=1:4,
		Sij=Sin(2+k);
		M_Sij=abs(Sij);
		P_Sij=uW_unwarp(Sij);
		
		M2_Sij=interp(frequence, f_Sij,M_Sij, splin(f_Sij,M_Sij,"monotone")); 
		P2_Sij=interp(frequence, f_Sij,P_Sij, splin(f_Sij,P_Sij,"monotone")); 
			
		Sin(2+k)=M2_Sij.*exp(%i*%pi*P2_Sij/180);
	end;
	
	S2=tlist(['S parameters';'frequency';'S11';'S12';'S21';'S22'],frequence,Sin.S11,Sin.S12,Sin.S21,Sin.S22);

endfunction
