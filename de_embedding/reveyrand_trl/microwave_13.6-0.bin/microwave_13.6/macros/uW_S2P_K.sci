function K=uW_S2P_K(S2P)
	K=(1-(abs(S2P.S11)).^2-(abs(S2P.S22)).^2+(abs(uW_S2P_DELTA(S2P))).^2)./(2*abs(S2P.S21).*abs(S2P.S12));
endfunction