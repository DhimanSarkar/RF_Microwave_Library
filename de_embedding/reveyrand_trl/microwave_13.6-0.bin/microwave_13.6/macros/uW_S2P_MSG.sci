// maximum stable gain : MSG (K<1)
function G=uW_S2P_MSG(S2P)
	K=uW_S2P_K(S2P);
	G=S2P.frequency.*0;
	G=G+(K<1);
	G=G.*(abs(S2P.S21)./abs(S2P.S12));
endfunction