// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2010

// filename="\\Aloha\Public sur Aloha\envoi_1\techn_\mesures\petit_signal\version_2\Spar_à_V1=0_et_V2=0\TXT100.CSV";

// ###########################
// # Lecture de fichier S2P
// ###########################

function S=uW_CSV_read(filename)
	// [M,text]=fscanfMat(filename);
	
	M=mgetl(filename);
	M=M(1:$-1);


	// Récupère le type de mesure
	Sij=grep(M,"MEAS")+1;
	Sij=tokens(M(Sij),",");
	Sij=Sij(2);

	// Récupère l'unité de fréquence
	unit=grep(M,"FREQUENCY")+1;
	data=unit+1;
	unit=tokens(M(unit),",");
	unit=unit(1);

	// Récupère les data en ohm
	M(data)="M=["+M(data)+";";
	M(data+1:$-1)=M(data+1:$-1)+";";
	M($)=M($)+"];";

	execstr(M(data:$));



	
	S=tlist(['S parameters';'frequency';'S11';'S12';'S21';'S22'],[],[],[],[],[]);
	

	S.frequency=M(:,1);
	data=M(:,2)+%i*M(:,3);
	gamma_=(data-50)./(data+50);
	execstr("S."+Sij+"=gamma_;");
	
endfunction

