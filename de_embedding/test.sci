thru = uW_S2P_read('D:\RF_Microwave_Library\de_embedding\cal_std\thru.s2p');
refl = uW_S2P_read('D:\RF_Microwave_Library\de_embedding\cal_std\refl.s2p');
line = uW_S2P_read('D:\RF_Microwave_Library\de_embedding\cal_std\line.s2p');

y = uW_TRL_calc(thru, line, refl, 'SHORT');