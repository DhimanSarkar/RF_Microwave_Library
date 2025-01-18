
function output=uW_S2P_stab(S)
	// Source Circle => Center and Radius
	C=(conj(S.S11-uW_S2P_DELTA(S).*conj(S.S22)))./( ((abs(S.S11)).^2)-((abs(uW_S2P_DELTA(S)))).^2);
	R=abs(abs(S.S12.*S.S21)./abs((abs(S.S11)).^2-(abs(uW_S2P_DELTA(S))).^2));
	output=[C,R]
endfunction