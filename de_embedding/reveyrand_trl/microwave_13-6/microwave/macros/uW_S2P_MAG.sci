//maximum available gain : MAG (K>1)
function G=uW_S2P_MAG(S2P)
	K=uW_S2P_K(S2P);
	G=S2P.frequency.*0;
	G=G+((K>1)&(K<1e6)).*(K-sqrt((K.^2)-1))+(K>=1e6).*(1 ./(2*K));
	G=G.*(abs(S2P.S21)./abs(S2P.S12));
	if (find(K<1)~=[]) then,
		printf("Warning : K<1\n");
	end;
endfunction