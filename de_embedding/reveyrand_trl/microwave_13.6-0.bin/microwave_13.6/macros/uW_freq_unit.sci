// ===========================
function k=uW_freq_unit(unit)
	U=["f";"p";"n";"u";"m";"z";"K";"M";"G";"T"];
	k=10.^([-15;-12;-9;-6;-3;0;3;6;9;12]);
	t=tokens(unit,"H");t=t(1);
	k=k(find(U==t))
endfunction

