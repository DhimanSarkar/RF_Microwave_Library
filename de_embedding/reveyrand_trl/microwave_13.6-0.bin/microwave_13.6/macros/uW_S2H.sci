// ################################################ //
// # TOOLBOX uW                                   # //
// #==============================================# //
// # Fonctions générales pour la gestion des S2P  # //
// # et de traitements de matrices [S]            # //
// ################################################ //



// ###########################################
// # Conversion d'une matrice 2 ports : S -> H
// ###########################################


function H=uW_S2H(S)
	freq=S.frequency;
	S11=S.S11;
	S12=S.S12;
	S21=S.S21;
	S22=S.S22;
	
	D=(1-S11).*(1+S22)+S12.*S21;
	H22=(1/50).*((1-S11).*(1-S22)-S12.*S21)./D;
	H21=(-2*S21)./D;
	H12=(2*S12)./D;
	H11=50.*((1+S11).*(1+S22)-S12.*S21)./D;
	
	H=tlist(['H parameters';'frequency';'H11';'H12';'H21';'H22'],freq,H11,H12,H21,H22);
endfunction
