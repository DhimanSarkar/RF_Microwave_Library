// Edwards-Sinsky stability parameter : µ1 
function u1=uW_S2P_u1(S2P)
	u1=(1-(abs(S2P.S11).^2))./( abs(S2P.S22-uW_S2P_DELTA(S2P).*conj(S2P.S11)) + abs(S2P.S12.*S2P.S21) );
endfunction