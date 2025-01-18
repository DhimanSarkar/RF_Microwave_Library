// 

function output=uW_S2P_to_SnP(file_list)
file2n=[1,2;3,3;6,4;10,5,;15,6;21,7;28,8;36,9];
i=find(file2n(:,1)==size(file_list,1));


if i~=[],
	n=file2n(i,2);
	cmd="SnP=tlist([''S parameters'';''frequency''";
	for i=1:n,
	for j=1:n,
	cmd=cmd+";"+''''+"S"+string(i)+string(j)+'''';
	end;
	end;
	cmd=cmd+"]";
	for i=1:n*n,
	cmd=cmd+",[]";
	end;
	cmd=cmd+");";
	execstr(cmd);


	index=n;
	index_file=1;
	S2P=uW_S2P_read(file_list(index_file));
	SnP.frequency=S2P.frequency;
	for i=1:(n-1),
			S2P=uW_S2P_read(file_list(index_file));
			cmd="SnP.S"+string(i)+string(i)+"=S2P.S11;"+"SnP.S"+string(i+1)+string(i+1)+"=S2P.S22;";
			execstr(cmd);
		for j=i+1:n,
			S2P=uW_S2P_read(file_list(index_file));
			cmd="SnP.S"+string(i)+string(j)+"=S2P.S12;"+"SnP.S"+string(j)+string(i)+"=S2P.S21;";
			execstr(cmd);
	    	index_file=index_file+1;
		end;
	end;
end;	
output=SnP;
endfunction		

