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


function Y=uW_Z2Y(Z)
freq_t=Y.frequency;
Z11=Z.Z11;
Z12=Z.Z12;
Z21=Z.Z21;
Z22=Z.Z22;

Y22=Z11./(Z11.*Z22-Z12.*Z21);
Y21=-Z21./(Z11.*Z22-Z12.*Z21);
Y12=-Z12./(Z11.*Z22-Z12.*Z21);
Y11=Z22./(Z11.*Z22-Z12.*Z21);
Y=tlist(['Y parameters';'frequency';'Y11';'Y12';'Y21';'Y22'],freq_t,Y11,Y12,Y21,Y22);
endfunction