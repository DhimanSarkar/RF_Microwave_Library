

function uW_S2P_stab_display(S)
	uW_display_vsmith([.2 .5 2 5],1);

	// Stability Circle INPUT : BLUE
	CR=uW_S2P_stab(S);
	C=CR(:,1);R=CR(:,2);
	xset("color",11);
	xarcs([real(C)-R,imag(C)+R,2*R,2*R,R*0,R*0+360*64].');

	// Stability Circle OUTPUT : RED
	CR=uW_S2P_stab(uW_S2P_flip(S));
	C=CR(:,1);R=CR(:,2);
	xset("color",21);
	xarcs([real(C)-R,imag(C)+R,2*R,2*R,R*0,R*0+360*64].');
	xset("color",1);
endfunction
