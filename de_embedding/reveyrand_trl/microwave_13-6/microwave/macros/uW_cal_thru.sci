// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2007



// #######################################
// # Génération d'un THRU idéal
// #######################################


function S=uW_cal_thru(freq)
	S11=freq*0;
	S21=S11+1;
	S=tlist(['S parameters';'frequency';'S11';'S12';'S21';'S22'],freq,S11,S21,S21,S11);
endfunction
