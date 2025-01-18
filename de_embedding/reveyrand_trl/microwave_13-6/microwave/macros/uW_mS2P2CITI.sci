
function uW_mS2P2CITI(varargin)

[lhs,rhs]=argn(0);
if rhs<2 then
	abort;
end;

filetype="None";
fileext="*.s2p";

measurement_directory=varargin(1);
filename_citi=varargin(2);
if rhs>2 then
	filetype=varargin(3);
	fileext="*.*";
end;



 // Conversion S2P directory to CITI
// S-IV measurements

 

// path="/home/tibo/Public/mesures/adeline/TV220880/";
// fichier_out=path+"measure.citi";

liste=dir(measurement_directory+fileext);
liste=liste.name;
n=size(liste,1);



 V1=[];
 I1=[];
 V2=[];
 I2=[];
 S11=[];
 S12=[];
 S21=[];
 S22=[];


  
  for i=1:n,

   filename=liste(i);
   [d,c]=fscanfMat(filename);

	if filetype=="DIVA" then,
   	   cc=c($-1);cc=part(cc,1:(length(cc)-1));
	   t=tokens(cc,[" ","="]);
	   _v1=evstr(t(2));
	   _v2=evstr(t(4));
	   _i1=evstr(t(3));
	   _i2=evstr(t(5));

	else,
	   cc=c(1);cc=part(cc,1:(length(cc)-1));
	   t=tokens(cc,[" ","="]);
	   _v1=evstr(t(1+find(t=="V1")));
	   _v2=evstr(t(1+find(t=="V2")));
	   _i1=evstr(t(1+find(t=="I1")));
	   _i2=evstr(t(1+find(t=="I2")));
	end;
   //_i2=evstr(part(t(9),1:(length(t(9))-1)));
   S=uW_S2P_read(filename);



 
   if S.frequency ~=[],
    freq_list=S.frequency;
 
    S11=[S11;string(abs(S.S11))+","+string(phasemag(S.S11))];
    S12=[S12;string(abs(S.S12))+","+string(phasemag(S.S12))];
    S21=[S21;string(abs(S.S21))+","+string(phasemag(S.S21))];
    S22=[S22;string(abs(S.S22))+","+string(phasemag(S.S22))];
 
    V1=[V1;string(_v1)];
    I1=[I1;string(_i1)];
    V2=[V2;string(_v2)];
    I2=[I2;string(_i2)];
   end;
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
  "BEGIN"];

data_inter=["END";
  "BEGIN"];

data_trans=[  "END";
  " ";
  entete2;"VAR_LIST_BEGIN";string(linspace(0,Index_meas-1,Index_meas).');
  "VAR_LIST_END";
  "VAR_LIST_BEGIN";
  "0";
  "VAR_LIST_END";
  "BEGIN"];

fd=mopen(filename_citi,"w");
	mputl(data_out,fd); 
	mputl(S11,fd);
	mputl(data_inter,fd); 
	mputl(S12,fd);
	mputl(data_inter,fd); 
	mputl(S21,fd);
	mputl(data_inter,fd); 
	mputl(S22,fd);
	mputl(data_trans,fd); 
	mputl(V1,fd);
	mputl(data_inter,fd); 
	mputl(I1,fd);
	mputl(data_inter,fd); 
	mputl(V2,fd);
	mputl(data_inter,fd); 
	mputl(I2,fd);
	mputl("END",fd);
mclose('all'); 

endfunction



 
