// path=SCI+"/contrib/uW/help/";
// txt = help_skeleton("uW_unwarp",path)

function uwp=uW_unwarp(Sij)
		x=phasemag(Sij(2:$))-phasemag(Sij(1:($-1)));
		a=(x<-200)*360+(x>200)*(-360);	// Seuil de discontinuité : 200°.
		a=cumsum(a,'r');
		a=[0;a];
		uwp=real(phasemag(Sij(1:$))+a);
endfunction
