
// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2007

// path=SCI+"/contrib/uW/help/";
// txt = help_skeleton("uW_MES_select_network",path);

// ###########################


function network=uW_MES_select_network(data)	
    liste_reseaux=[];
	for i=1:size(data.network),
	
		// Lecture point de repos 1ere courbe + Temperature
		value=uW_MES_get_quiescent(data,i);
		value=int(value*10)/10;
		
		// Dérivée présente ?
		derivee="-";
		if (data.network(i).curve(1).plot(1).di2dv1~=[]) then,
			derivee="d";
		end;
		
		// Intrisèques présents ?
		intrinsic="-";
		if (data.network(i).curve(1).plot(1).Cgs~=[]) then,
			intrinsic="i";
		end;
		
		ligne="["+intrinsic+derivee+"-] ("+string(size(data.network(i).curve))+") : "+string(value(1))+"V / "+string(value(3))+"V" + " ("+string(int(value(4)))+"mA)"+ " - ["+string(value(5)-273)+"°]";
		liste_reseaux=[liste_reseaux;ligne];
	end;
	network=x_choose(liste_reseaux,['Select an IV-network']); 
endfunction
