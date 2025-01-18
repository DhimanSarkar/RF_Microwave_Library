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
// # Génération du S11 d'un standard
// #######################################

function S=uW_cal_standard(f,std)
	Zo=50;
	select typeof(std),
	case "Open standard",
		Ceff=std.C0+std.C1*f+std.C2*f.^2+std.C3*f^3;
		S11=(1-%i*100*%pi*f.*Ceff)./(1+%i*100*%pi*f.*Ceff);
	case "Short standard",
		Leff=std.L0+std.L1*f+std.L2*f.^2+std.L3*f^3;
		S11=(%i*2*%pi*f.*Leff-50)./(%i*2*%pi*f.*Leff+50);
	case "Match standard",
		Z=std.R0+%i*2*%pi*std.L0;
		S11=(Z-50)./(Z+50);
	end;
	
	Loss=exp( (-std.delay/Zo)*std.loss*sqrt(f./(10^9)) );
	Delay=exp(-%i*4*%pi*std.delay*f);
	S11=Loss.*Delay.*S11;
	
	S=tlist(['S parameters';'frequency';'S11'],f,S11);
endfunction
