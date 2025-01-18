// ################################################ //
// # TOOLBOX uW                                   # //
// #==============================================# //
// # Fonctions générales pour la gestion des S2P  # //
// # et de traitements de matrices [S]            # //
// ################################################ //


// ================================================ //
// T.Reveyrand     2007                             //
// v. 0.1                                           //
// ================================================ //




// #######################################
// # Affichage d'un S1P ou S2P
// #######################################









function uW_S2P_display(varargin)

	[lhs,rhs]=argn(0);
	nb_par=size(varargin(1)(1)(3:$),"r");
 
	impedance_lines=[.2 .5 1 2 5];
	smith_color=12;
	clf;


	select nb_par,
	case 1,
		uW_display_smith(impedance_lines,smith_color);
		for i=1:rhs,
			plot2d(real(varargin(i).S11),imag(varargin(i).S11),i);
		end;
	case 4,
	
	subplot(2,2,1);
	
	
	uW_display_smith(impedance_lines,smith_color);
	for i=1:rhs,
	plot2d(real(varargin(i).S11),imag(varargin(i).S11),i);
	end;
	
	subplot(4,2,2);

	for i=1:rhs,
	plot2d(varargin(i).frequency/10^9,20*log10(%eps+abs(varargin(i).S12)),i);
	end;

	
	
	subplot(4,2,4)

	for i=1:rhs,
	plot2d(varargin(i).frequency/10^9,phasemag(varargin(i).S12),i);
	end;
	
	subplot(4,2,5)
	// ====== Affichage du Module S21	

	for i=1:rhs,
	plot2d(varargin(i).frequency/10^9,20*log10(%eps+abs(varargin(i).S21)),i);
	end;
	
	subplot(4,2,7)
	// ====== Affichage de la phase S21	

	for i=1:rhs,
	plot2d(varargin(i).frequency/10^9,phasemag(varargin(i).S21),i);
	end;
	
	// ==========================
	
	subplot(2,2,4)

	
	
	uW_display_smith(impedance_lines,smith_color);
	for i=1:rhs,
	plot2d(real(varargin(i).S22),imag(varargin(i).S22),i);
	end;

	// ==========================

	end;
	
endfunction

