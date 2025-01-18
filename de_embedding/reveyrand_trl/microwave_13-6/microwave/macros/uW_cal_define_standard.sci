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
// # Definition d'un standard d'étalonnage
// #######################################


function standard=uW_cal_define_standard(mytype,varargin)
	[lhs,rhs]=argn(0);
	
	// 
	delay=0;
	loss=0;
	data=[0,0,0,0];
	index=1;
	// Si delay ou loss sont spécifiés : affecter les valeurs
	for i=1:(rhs-1),
		getit=%t;
		
		if grep(string(varargin(i)),"delay="),
			execstr(varargin(i)+";");
			getit=%f;
		end;
		
		if grep(string(varargin(i)),"loss="),
			execstr(varargin(i)+";");
			getit=%f;
		end;
		
		if (getit==%t)&(index<5),
			data(index)=data(index)+varargin(i);
			index=index+1;
		end;
		
	end;
	// 

 
	
	select mytype,
	case "O",
		C=data;
		standard=tlist(['Open standard';'C0';'C1';'C2';'C3';'delay';'loss'],C(1),C(2),C(3),C(4),delay,loss);
	case "S",
		L=data;
		standard=tlist(['Short standard';'L0';'L1';'L2';'L3';'delay';'loss'],L(1),L(2),L(3),L(4),delay,loss);
	case "L",
		R=data;
		standard=tlist(['Match standard';'R0';'L0';'delay';'loss'],R(1),R(2),delay,loss);
	end;
	
endfunction
