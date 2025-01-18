// ################################################ //
// # TOOLBOX uW                                   # //
// #==============================================# //
// # Fonctions générales pour la gestion des S2P  # //
// # et de traitements de matrices [S]            # //
// ################################################ //



// ###########################################
// # Conversion d'une matrice 2 ports : S -> Z
// ###########################################


function Z=uW_S2Z(S)
	freq=S.frequency;
	S11=S.S11;
	S12=S.S12;
	S21=S.S21;
	S22=S.S22;
	
	C=(50)./((1-S11).*(1-S22)-S12.*S21);
	Z22=C.*((1-S11).*(1+S22)+S12.*S21);
	Z21=C.*(2*S21);
	Z12=C.*(2*S12);
	Z11=C.*((1+S11).*(1-S22)+S12.*S21);
	
	Z=tlist(['Z parameters';'frequency';'Z11';'Z12';'Z21';'Z22'],freq,Z11,Z12,Z21,Z22);
endfunction
