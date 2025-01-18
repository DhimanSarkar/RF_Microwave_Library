

// Edwards-Sinsky stability parameter : µ1 and µ2

function u2=uW_S2P_u2(S2P)
	S=uW_S2P_flip(S2P);
	u2=uW_S2P_u1(S);
endfunction
