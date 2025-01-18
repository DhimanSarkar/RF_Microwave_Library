// Flip port 1 <-> port 2
function S=uW_S2P_flip(S)
	S11=S.S11;
	S12=S.S12;
	S21=S.S21;
	S22=S.S22;	

	S.S22=S11;
	S.S11=S22;
	S.S12=S21;
	S.S21=S12;
endfunction