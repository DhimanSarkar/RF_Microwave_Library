
function uW_MES2CITI(filename_mes,filename_citi)

 filename_mps=tokens(filename_mes,[":"," ","\","/"]);

 filename_mps=filename_mps($);
 path=part(filename_mes,[1:length(filename_mes)-length(filename_mps)]);
 

 dataset = uW_MES_read(filename_mes);

 row=grep(dataset.info,"mps"); 
 filename_mps=tokens(dataset.info(row),[":"," ","\","/"]);
 filename_mps=filename_mps($);
 filename_mps=path+filename_mps;

 network = uW_MES_select_network(dataset);


 V1=[];
 I1=[];
 V2=[];
 I2=[];
 S11=[];
 S12=[];
 S21=[];
 S22=[];

 // Un seul réseau

 nb_curve=size(dataset.network(network).curve);

 winId=waitbar('Converting MES file');

 for i=1:nb_curve,
  nb_pts=size(dataset.network(network).curve(i).plot);
  for j=1:nb_pts,
 
 
   index=dataset.network(network).curve(i).plot(j).S2P;
   S = uW_MPS_read(filename_mps,index);
 
   if S.frequency ~=[],
    freq_list=S.frequency;
 
    S11=[S11;string(abs(S.S11))+","+string(phasemag(S.S11))];
    S12=[S12;string(abs(S.S12))+","+string(phasemag(S.S12))];
    S21=[S21;string(abs(S.S21))+","+string(phasemag(S.S21))];
    S22=[S22;string(abs(S.S22))+","+string(phasemag(S.S22))];
 
    V1=[V1;string(dataset.network(network).curve(i).plot(j).v1)];
    I1=[I1;string(dataset.network(network).curve(i).plot(j).i1)];
    V2=[V2;string(dataset.network(network).curve(i).plot(j).v2)];
    I2=[I2;string(dataset.network(network).curve(i).plot(j).i2)];
   end;
  end;
 waitbar(i/nb_curve,winId);
 end;

 

 Index_meas=size(V1,1);

 

 // Sauvegarde

 


 

 entete=[ "CITIFILE A.01.00";
   "NAME IV_Meas.SP";
   "VAR Index_meas MAG "+string(Index_meas);
   "VAR freq MAG "+string(size(freq_list,1));
   "DATA S[1,1] MAGANGLE";
   "DATA S[1,2] MAGANGLE";
   "DATA S[2,1] MAGANGLE";
   "DATA S[2,2] MAGANGLE"];

 

 entete2=[ "CITIFILE A.01.00";
   "NAME IV_Meas.DC";
   "VAR Index_meas MAG "+string(Index_meas);
   "VAR freq MAG 1";
   "DATA V1 MAG";
   "DATA I1 MAG";
   "DATA V2 MAG";
   "DATA I2 MAG"];

 

 data_out=[entete;"VAR_LIST_BEGIN";string(linspace(0,Index_meas-1,Index_meas).');
  "VAR_LIST_END";
  "VAR_LIST_BEGIN";
  strsubst(string(freq_list),"D","e");
  "VAR_LIST_END";
  "BEGIN";
  S11;
  "END";
  "BEGIN";
  S12;
  "END";
  "BEGIN";
  S21;
  "END";
  "BEGIN";
  S22;
  "END";
  " ";
  entete2;"VAR_LIST_BEGIN";string(linspace(0,Index_meas-1,Index_meas).');
  "VAR_LIST_END";
  "VAR_LIST_BEGIN";
  "0";
  "VAR_LIST_END";
  "BEGIN";
  V1;
  "END";
  "BEGIN";
  I1;
  "END";
  "BEGIN";
  V2;
  "END";
  "BEGIN";
  I2;
  "END"];

 mputl(data_out,filename_citi);  
winclose(winId);
endfunction
