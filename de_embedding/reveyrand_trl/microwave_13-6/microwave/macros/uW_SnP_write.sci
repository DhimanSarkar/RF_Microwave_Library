

function uW_SnP_write(S_parameters,fichier,commentaire)


	// format("v");
	SnP=S_parameters;
	n=sqrt(size(SnP)-2);

	cmd="M1=[SnP.frequency";
	for i=1:n,
	for j=1:n,
	cmd=cmd+",SnP.S"+string(i)+string(j);
	end;
	end;
	cmd=cmd+"];";
	execstr(cmd);

    // M1=S_parameters;
	M2=M1(:,2:$);
	M2=matrix(M2.',n,n*size(M1,1)).';
	M3=[];
   for i=1:(size(M2,"c")),
       MAG=abs(M2(:,i));
       ARG=phasemag(M2(:,i));
       M3=M3+string(MAG)+" "+string(ARG)+" ";
   end;
	freq_=[M1(:,1),M1(:,1)*zeros(1,n-1)];
	freq_=matrix([M1(:,1),M1(:,1)*zeros(1,n-1)].',n*size(M1,1),1);
	i=find(freq_==0);
	// format("e",12);
	M4=string(freq_)+" ";
	M4(i)=" ";
	M4=strsubst(M4,"D","e");
	M5=M4+M3;
	M5=["! "+commentaire;"# HZ S MA R 50";M5]
	disp(M5)
	fd=mopen(fichier,"w");
	mputl(M5,fd);
	mclose(fd);
	// format("v");

endfunction 


