// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2008

// path=SCI+"/contrib/uW/help/";
// txt = help_skeleton("uW_MPS_read",path);


// ###########################
// # Lecture de fichier MPS (banc de mesure IV pulsé)
// ###########################

function S=uW_MPS_read(mps_filename,mps_index)
		
	// Debugage
	// mps_filename="C:\USERS\tibo\modele\QQ_R2_LNA\Q3-2x125\15V20%\2x125.mps";
	//	mps_index="BL1";
	//  S=uW_MPS_read(mps_filename,mps_index);
	//  uW_S2P_display(S); 	
		
	mps_data=mgetl(mps_filename);//lecture du fichier mes

	// Recupere les parametres [S]
	index=grep(mps_data,"!!"+mps_index);
	
	data=[];

	
	if (index~=[]) then,
		data=mps_data(index+5:$);
		index_fin=min(grep(data,"!!"));
		data=data(1:index_fin-1);

		data(1)="data=["+data(1)+";";
		data(2:$-1)=data(2:$-1)+";";
		data($)=data($)+"];";

		execstr(data);

		for i=1:4
			data(:,i+1)=data(:,2*i).*exp(%i*(data(:,2*i+1)/180)*%pi);
		end;
		data=data(:,1:5);
	end;
	
	// conversion de la table en objet parametre S
	// data(:,1)=data(:,1)*10^9;
	
	
	S=tlist(['S parameters';'frequency';'S11';'S12';'S21';'S22'],[],[],[],[],[]);
	S.frequency=data(:,1)*10^9;
	S.S11=data(:,2);
	S.S21=data(:,3);
	S.S12=data(:,4);
	S.S22=data(:,5);
	
	

	
endfunction

