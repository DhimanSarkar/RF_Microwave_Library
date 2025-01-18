// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2007



// ################################
// # Affichage de l'abaque de Smith
// ################################

function uW_display_smith(impedance_lines,mycolor)
	plot2d([-1 1],[0 0],mycolor)
	tr = 2*%pi*(0:.01:1);
	for r = impedance_lines  
		rr = 1/(r+1);
		cr = 1-rr;
		plot2d(cr+rr*cos(tr),rr*sin(tr),mycolor)
	end
	plot2d(cos(tr),sin(tr),mycolor)
	for x = impedance_lines   
		rx = 1/x;
		cx = rx;
		tx = 2*atan(x)*(0:.01:1);
		plot2d(1-rx*sin(tx),cx-rx*cos(tx),mycolor)
		plot2d(1-rx*sin(tx),-cx+rx*cos(tx),mycolor)
	end
endfunction
