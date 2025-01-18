
function varargout=uW_S2P_split(varargin)

	[lhs,rhs]=argn(0);
	// nb_par=size(varargin(1)(1)(3:$),"r");
	// disp(rhs);
	// S=0;
	select rhs,
	
		// Input "Thru S2P" data only
		case 1 then,
			Stotal=varargin(1);
			
			// Création des paramètres S
			Sin=tlist(['S parameters';'frequency';'S11';'S12';'S21';'S22'],[],[],[],[],[]);
			Sin.frequency=Stotal.frequency;
			Sout=Sin;
			
	
			Sin.S11=Stotal.S11;
			Sout.S22=Stotal.S22;
			Sin.S22=Stotal.S11.*0;
			Sout.S11=Sin.S22;
			
			// Calcul des S21 
			module=abs(sqrt(abs(Stotal.S21)));
			phase=uW_unwarp(Stotal.S21);
			
			// Determine la phase à l'origine
			po=phase(2)-((phase(1)-phase(2))/(Stotal.frequency(1)-Stotal.frequency(2))) *Stotal.frequency(2);
			phase=phase-int(po./360)		
			// if (pmodulo(po,360)>180) then phase=phase-360; end;
			phase=phase/2;
			
			
			Sin.S21=module.*exp(%i*phase*%pi/180);
			Sout.S21=Sin.S21;
			
			// Calcul des S12
			module=abs(sqrt(abs(Stotal.S12)));
			phase=uW_unwarp(Stotal.S12);
			
			// Determine la phase à l'origine
			po=phase(2)-((phase(1)-phase(2))/(Stotal.frequency(1)-Stotal.frequency(2))) *Stotal.frequency(2);
			phase=phase-int(po./360)		
			// if (pmodulo(po,360)>180) then phase=phase-360; end;
			phase=phase/2;
			
			Sin.S12=module.*exp(%i*phase*%pi/180);
			Sout.S12=Sin.S12;
			
			varargout=list(Sin,Sout);
		
		
		
		
		
		
		
	
		// Input "Thru S2P" and "Open S2P" 
		case 2 then,
			Stotal=varargin(1);
			Sopen=varargin(2);
			
			// Grill de fréquence identique ?
			if find((Stotal.frequency==Sopen.frequency)==%F) ~=[],
				disp("Warning : Frequency grids are not the same.");
				varargout=list([]);
			else,	
				
			
			
			// Création des paramètres S
			Sin=tlist(['S parameters';'frequency';'S11';'S12';'S21';'S22'],[],[],[],[],[]);
			Sin.frequency=Stotal.frequency;
			Sout=Sin;
			Open=tlist(['S parameters';'frequency';'S11'],[],[]);
			Open.frequency=Sin.frequency;
	
			Sin.S11=Stotal.S11;
			Sout.S22=Stotal.S22;
			Sin.S22=Stotal.S11.*0;
			Sout.S11=Sin.S22;
			
			// Calcul de Sin21*Sin12 => inconnue du signe
			X=sqrt((Stotal.S21.*Stotal.S12).*(Sopen.S11./Sopen.S22));
			Gamma=Sopen.S11./X;
			
			// Tri des bonnes solutions
			indice_faux=find(real(Gamma)<0);
			X(indice_faux)=-X(indice_faux);
			Open.S11=Sopen.S11./X;
			
			// X=S21in * S12in
			
			// Calcul du module
			module=abs(sqrt(abs(X)));
			
			// Estimation de la phase
			phase=uW_unwarp(X);
			
			//    Determine la phase à l'origine
			po=phase(2)-((phase(1)-phase(2))/(Stotal.frequency(1)-Stotal.frequency(2))) *Stotal.frequency(2);
			phase=phase-int(po./360)		
			// if (pmodulo(po,360)>180) then phase=phase-360; end;
			
			// Phase déroulée de S21 et S12
			phase=phase/2;
			
			Sin.S21=module.*exp(%i*phase*%pi/180);
			Sin.S12=Sin.S21;
			
			Sout.S21=Stotal.S21./Sin.S21;
			Sout.S12=Stotal.S12./Sin.S12;
			
			
			varargout=list(Sin,Sout,Open);
			end;
		
	end;
	

endfunction




