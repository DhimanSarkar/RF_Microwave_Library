function S_DUT=uW_S2P_deembedding(S_Total,Sin,Sout)

	// Spline de Sin et Sout
	frequence=S_Total.frequency;
	
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
	
	// Sout
		f_Sij=Sout.frequency;
	for k=1:4,
		Sij=Sout(2+k);
		M_Sij=abs(Sij);
		P_Sij=uW_unwarp(Sij);
		
		M2_Sij=interp(frequence, f_Sij,M_Sij, splin(f_Sij,M_Sij,"monotone")); 
		P2_Sij=interp(frequence, f_Sij,P_Sij, splin(f_Sij,P_Sij,"monotone")); 
			
		Sout(2+k)=M2_Sij.*exp(%i*%pi*P2_Sij/180);
	end;
	
	
	// Calcul pour chaque frequence du S_DUT
	
	S11=[];
	S21=[];
	S12=[];
	S22=[];
	
	for i=1:length(S_Total.frequency),
		
		
		// Lecture des Sin et Sout
		S11A=Sin.S11(i);
		S12A=Sin.S12(i);
		S21A=Sin.S21(i);
		S22A=Sin.S22(i);
		
		S11B=Sout.S11(i);
		S12B=Sout.S12(i);
		S21B=Sout.S21(i);
		S22B=Sout.S22(i);
		
		
		// Calcul de TA^(-1) et TB^(-1) => Sdut
		TAI=(1/S12A)*[(-S11A*S22A+S12A*S21A),S22A;-S11A,1];
		TBI=(1/S12B)*[(-S11B*S22B+S12B*S21B),S22B;-S11B,1];
		Ttotal=(1/S_Total.S21(i))*[1,(-1)*S_Total.S22(i);S_Total.S11(i),(S_Total.S12(i)*S_Total.S21(i)-S_Total.S11(i)*S_Total.S22(i))];
		Tdut=TAI*Ttotal*TBI;
		Sdut=(1/Tdut(1,1))*[Tdut(2,1),Tdut(1,1)*Tdut(2,2)-Tdut(2,1)*Tdut(1,2);1,(-1)*Tdut(1,2)];
		
		S11=[S11;Sdut(1,1)];
		S21=[S21;Sdut(2,1)];
		S12=[S12;Sdut(1,2)];
		S22=[S22;Sdut(2,2)];
	end;

	S_DUT=tlist(['S parameters';'frequency';'S11';'S12';'S21';'S22'],S_Total.frequency,S11,S12,S21,S22);
		
	
	


endfunction