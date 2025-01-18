

function uW_display_vsmith(scale,mycolor);
	
	 plot2d(0,0,-1,"031"," ",[-1,-1,1,1])
	 xset("color",mycolor);

	// Tri du vecteur scale
	a=size(scale); 
	if a(1)>a(2) then, scale=scale'; end;	// vecteur ligne seulement
	scale=abs(scale);			// Valeur absolue
	vect=scale(find((scale~=1)&(scale~=0)));	// Enleve 0 et 1 si présents
	vect=scale;
	 vect(1,$+1)=1;


	// Parties Reelles
	 scale=vect;
	scale(1,$+1)=0;

	k=(scale-1)./(scale+1);
	arcs=k;
	arcs(2,:)=0.5-k/2;
	arcs(3,:)=1-k;
	arcs(4,:)=1-k;
	arcs(5,:)=0;
	arcs(6,:)=360*64;
	xarcs(arcs);

	// Partie IM > 0
	 scale=vect;

	z=(%i*scale-1)./(%i*scale+1);;
	rayon=((real(z)-1)^2+imag(z)^2)./(2*imag(z));
	phase=(1+%i*rayon)-z;phase=atan(imag(phase),real(phase));
	arcs=1-rayon;
	arcs(2,:)=2*rayon;
	arcs(3,:)=2*rayon;
	arcs(4,:)=2*rayon;
	arcs(5,:)=((phase/%pi)*180+180)*64;  // form
	arcs(6,:)=270*64-arcs(5,:);
	xarcs(arcs);

	// Partie IM < 0
	// z=Gamma_R(%i*scale);
	rayon=((real(z)-1)^2+imag(z)^2)./(2*imag(z));
	phase=(1+%i*rayon)-z;phase=-atan(imag(phase),real(phase));
	arcs=1-rayon;
	arcs(2,:)=0;
	arcs(3,:)=2*rayon;
	arcs(4,:)=2*rayon;
	arcs(5,:)=90*64;
	arcs(6,:)=(360+(phase/%pi)*180-90-180)*64;  // form
	xarcs(arcs);


	// Partie IM = 0
	xsegs ([-1,1],[0,0])

endfunction;
