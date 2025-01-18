// ################################################ //
// # TOOLBOX uW                                   # //
// #==============================================# //
// # Fonctions générales pour la gestion des S2P  # //
// # et de traitements de matrices [S]            # //
// ################################################ //
// T. Reveyrand
// www.microwave.fr
// ----
// Updated by Sebastian Luis Rubio Ayala


// ###########################################
// # Conversion d'une matrice 2 ports : S -> Y
// ###########################################


function Y=uW_S2Y(S)
freq_t=S.frequency;
S11=S.S11;
S12=S.S12;
S21=S.S21;
S22=S.S22;
C=1 ./(50*((1+S11).*(1+S22)-S12.*S21));
Y22=C.*((1+S11).*(1-S22)+S12.*S21);
Y21=C.*(-2*S21);
Y12=C.*(-2*S12);
Y11=C.*((1-S11).*(1+S22)+S12.*S21);
Y=tlist(['Y parameters';'frequency';'Y11';'Y12';'Y21';'Y22'],freq_t,Y11,Y12,Y21,Y22);
endfunction