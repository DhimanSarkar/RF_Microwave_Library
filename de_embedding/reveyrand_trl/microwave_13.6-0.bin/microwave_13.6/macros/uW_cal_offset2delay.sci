// ################################################ //
// # TOOLBOX uW                                   # //
// #==============================================# //
// # Fonctions générales pour la gestion des S2P  # //
// # et de traitements de matrices [S]            # //
// ################################################ //


// ================================================ //
// T.Reveyrand     2007                             //
// v. 0.1                                           //
// ================================================ //




// ###########################################
// # Conversion d'un offset de CALKIT en Delay
// ###########################################


function t=uW_cal_offset2delay(l)
	c=3*10^8;	// celerité
	l=l/1000;	// l mm -> m
	t=l/c;		// Approx. faite ds le programme HP VEE
endfunction
