
// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2007

// path=SCI+"/contrib/uW/help/";
// txt = help_skeleton("uW_MES_get_quiescent",path);

// ###########################

function value=uW_MES_get_quiescent(mes,i)
		temp=mes.network(i).info(grep(mes.network(i).info,"TK"));
		tindex=strindex(temp,"TK");
	
		info=mes.network(i).curve(1).info(grep(mes.network(i).curve(1).info,"Point repos:"));
		index=strindex(info ,["! Point repos: Vgs ";"Ig";"Vds";"Id"]);
		value=evstr("["+part(info,[[(index(1)+19):(index(2)-1)],[(index(2)+2):(index(3)-1)],[(index(3)+3):(index(4)-1)],[(index(4)+2):(length(info))]])+"]");
		
		// Met les courant en mA
		value(2)=value(2)*1000;
		value(4)=value(4)*1000;
		
		// Ajoute la température
		value=[value,evstr(part(temp,[tindex+3:length(temp)]))]; 
endfunction
