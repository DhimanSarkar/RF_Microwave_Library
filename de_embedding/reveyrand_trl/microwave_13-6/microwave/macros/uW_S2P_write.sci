// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2007



// ###########################
// # Lecture de fichier S2P
// ###########################

function uW_S2P_write(S_parameters,fichier,commentaire)
   S2P=S_parameters;
   M1=[S2P.frequency,S2P.S11,S2P.S21,S2P.S12,S2P.S22];
   // M1=S_parameters;
   M2=M1(:,1);
   for i=1:(size(M1,"c")-1),
       MAG=abs(M1(:,i+1));
       ARG=phasemag(M1(:,i+1));
       M2=[M2,[MAG,ARG]];
   end;
   format_donnees="%f";
   text="! "+commentaire;
   entete="# HZ S MA R 50";
   text=[text;entete];
   fprintfMat(fichier,real(M2),format_donnees,text)
endfunction 
