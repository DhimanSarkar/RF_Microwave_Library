clear;
clc;

exec("D:\RF_Microwave_Library\de_embedding\reveyrand_trl\microwave_13-6\microwave\macros\uW_S2P_read.sci");
exec("D:\RF_Microwave_Library\de_embedding\reveyrand_trl\microwave_13-6\microwave\macros\uW_S2P_write.sci");
exec("D:\RF_Microwave_Library\de_embedding\reveyrand_trl\microwave_13-6\microwave\macros\uW_TRL_calc.sci");
exec("D:\RF_Microwave_Library\de_embedding\reveyrand_trl\microwave_13-6\microwave\macros\uW_S2T.sci");
exec("D:\RF_Microwave_Library\de_embedding\reveyrand_trl\microwave_13-6\microwave\macros\uW_T2S.sci");
exec("D:\RF_Microwave_Library\de_embedding\reveyrand_trl\microwave_13-6\microwave\macros\uW_S2P_deembedding.sci");
exec("D:\RF_Microwave_Library\de_embedding\reveyrand_trl\microwave_13-6\microwave\macros\uW_unwarp.sci");
exec("D:\RF_Microwave_Library\de_embedding\reveyrand_trl\microwave_13-6\microwave\macros\uW_S2P_display.sci");
exec("D:\RF_Microwave_Library\de_embedding\reveyrand_trl\microwave_13-6\microwave\macros\uW_display_smith.sci");

// thru = uW_S2P_read('D:\RF_Microwave_Library\de_embedding\cal_std\sim\thru.s2p');
// refl = uW_S2P_read('D:\RF_Microwave_Library\de_embedding\cal_std\sim\refl.s2p');
// line = uW_S2P_read('D:\RF_Microwave_Library\de_embedding\cal_std\sim\line.s2p');
thru = uW_S2P_read('D:\RF_Microwave_Library\de_embedding\cal_std\focus_TRL\thru.s2p');
refl = uW_S2P_read('D:\RF_Microwave_Library\de_embedding\cal_std\focus_TRL\refl.s2p');
line = uW_S2P_read('D:\RF_Microwave_Library\de_embedding\cal_std\focus_TRL\line.s2p');

y = uW_TRL_calc(thru, line, refl, 'SHORT');
uW_S2P_write(y,'D:\RF_Microwave_Library\de_embedding\cal_std\focus_TRL\fix_code.s2p','fixture-S')
uW_S2P_display(y)

