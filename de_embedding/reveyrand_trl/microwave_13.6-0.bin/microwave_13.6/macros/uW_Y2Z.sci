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


function Z=uW_Y2Z(Y)
freq_t=Y.frequency;
Y11=Y.Y11;
Y12=Y.Y12;
Y21=Y.Y21;
Y22=Y.Y22;

Z22=Y11./(Y11.*Y22-Y12.*Y21);
Z21=-Y21./(Y11.*Y22-Y12.*Y21);
Z12=-Y12./(Y11.*Y22-Y12.*Y21);
Z11=Y22./(Y11.*Y22-Y12.*Y21);
Z=tlist(['Z parameters';'frequency';'Z11';'Z12';'Z21';'Z22'],freq_t,Z11,Z12,Z21,Z22);
endfunction