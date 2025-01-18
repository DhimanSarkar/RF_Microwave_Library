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



function S=uW_Z2S(Z)
freq_t=Z.frequency;
Z11=Z.Z11;
Z12=Z.Z12;
Z21=Z.Z21;
Z22=Z.Z22;
Z0=50; //Characteristic impedance at each port (assumed the same for the two ports)
C=((Z11+Z0).*(Z22+Z0))-(Z12.*Z21);
S22=((Z11+Z0).*(Z22-Z0)-(Z12.*Z21))./C;
S21=(2.*Z0.*Z21)./C;
S12=(2.*Z0.*Z12)./C;
S11=((Z11-Z0).*(Z22+Z0)-(Z12.*Z21))./C;
S=tlist(['S parameters';'frequency';'S11';'S12';'S21';'S22'],freq_t,S11,S12,S21,S22);
endfunction
