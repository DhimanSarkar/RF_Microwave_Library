// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2007



// ###########################
// # Lecture de fichier S1P
// ###########################

function uW_S1P_write(S_parameters,fichier,commentaire)
   S1P=S_parameters;
   M1=[S1P.frequency,S1P.S11];
   // M1=S_parameters;
   M2=M1(:,1);
   MAG=abs(M1(:,2));
   ARG=phasemag(M1(:,2));
   M2=[M2,[MAG,ARG]];
  
   format_donnees="%f";
   text="! "+commentaire;
   entete="# HZ S MA R 50";
   text=[text;entete];
   fprintfMat(fichier,real(M2),format_donnees,text)
endfunction 
