// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2008

// path=SCI+"/contrib/uW/help/";
// txt = help_skeleton("uW_S2P_unoise",path);


// ###########################
// # Débruitage d'un S2P
// ###########################

function S2=uW_S2P_unoise(S1)


// Debruitage

M=[S1.S11,S1.S21,S1.S12,S1.S22];
F=S1.frequency/10^9;

SYS=[];
for i=[-2,-1,-0.5,-1/3,0,1/3,1/2,1,2],
	SYS=[SYS,(F.^(i))];
end;

_M=[];
for m=1:4,
	SOL=pinv(SYS)*M(:,m);
	_M=[_M,SYS*SOL];
end;

S2=S1;
S2.S11=_M(:,1);
S2.S21=_M(:,2);
S2.S12=_M(:,3);
S2.S22=_M(:,4);

endfunction;
