// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2007



// ###########################
// # Lecture de fichier S2P
// ###########################

function S=uW_S2P_read(filename)
	[M,text]=fscanfMat(filename);
	
	
	
	S=tlist(['S parameters';'frequency';'S11';'S12';'S21';'S22'],[],[],[],[],[]);
	
	// unit renvoie le vecteur des unités
	// value est le vecteur des quantités
	unit=tokens(text(find(part(text,1)=="#"))," ");
	
	// value=tokens(text($)," ");
	// i=0;
	// while (length(value)<2),  
	//	i=i+1;
	//	value=tokens(text($-i)," ");
	// end;
	
	value=unit;
	
	
	if value==unit then
		// FORMAT JP / IV CAD
		S.frequency=M(:,1);
		
		unit_text=["HZ" "kHZ" "MHZ" "GHZ"];
		unit_value=(10^9)*[10^(-9) 10^(-6) 10^(-3) 1];
		S.frequency=S.frequency*unit_value( find(unit_text==convstr(unit(2),"u")) );
		
		
		select(convstr(unit(4),"u")),
			case "MA" then,
				S.S11=M(:,2).*exp((%i*%pi/180)*M(:,3));
				S.S12=M(:,6).*exp((%i*%pi/180)*M(:,7));
				S.S21=M(:,4).*exp((%i*%pi/180)*M(:,5));
				S.S22=M(:,8).*exp((%i*%pi/180)*M(:,9));
			
			case "DB" then,
				S.S11=uW_dB2lin(M(:,2)).*exp((%i*%pi/180)*M(:,3));
				S.S12=uW_dB2lin(M(:,6)).*exp((%i*%pi/180)*M(:,7));
				S.S21=uW_dB2lin(M(:,4)).*exp((%i*%pi/180)*M(:,5));
				S.S22=uW_dB2lin(M(:,8)).*exp((%i*%pi/180)*M(:,9));
		
			case "RI" then,
			// Il peut arriver que le S2P soit exprimé en Reel / Imag...
			//
			//
				S.S11=M(:,2)+%i*M(:,3);
				S.S12=M(:,6)+%i*M(:,7);
				S.S21=M(:,4)+%i*M(:,5);
				S.S22=M(:,8)+%i*M(:,9);
		
		
	
		end;
	
	else
	
	

	
		// FORMAT ANRITSU + ADS
		
		// Copie les données
		index_data=find(convstr(value,"u")=="FREQ")-1;
		S.frequency=M(:,index_data);
		
		// Met la frequence en GHz
	
		unit_text=["HZ" "KHZ" "MHZ" "GHZ"];
		unit_value=(10^9)*[10^(-9) 10^(-6) 10^(-3) 1];
		S.frequency=S.frequency*unit_value( find(unit_text==convstr(unit(2),"u")) );
	
		// Les données sont-elles en reel/imag ou en mag phase ?
	

		select(convstr(unit(4),"u")),
			case "MA" then,
			
				MS11=find((value=="magS11")|(value=="S11M"));
				MS21=find((value=="magS21")|(value=="S21M"));
				MS12=find((value=="magS12")|(value=="S12M"));
				MS22=find((value=="magS22")|(value=="S22M"));				
			
				PS11=find((value=="angS11")|(value=="S11A"));
				PS21=find((value=="angS21")|(value=="S21A"));
				PS12=find((value=="angS12")|(value=="S12A"));
				PS22=find((value=="angS22")|(value=="S22A"));	
			
				S.S11=M(:,MS11-1).*exp((%i*%pi/180)*M(:,PS11-1));
				S.S12=M(:,MS12-1).*exp((%i*%pi/180)*M(:,PS12-1));
				S.S21=M(:,MS21-1).*exp((%i*%pi/180)*M(:,PS21-1));
				S.S22=M(:,MS22-1).*exp((%i*%pi/180)*M(:,PS22-1));

		
			// case "RI" then,
			// Il peut arriver que le S2P soit exprimé en Reel / Imag...
			//
			//
		
		
	
		end;
	end;
	
endfunction

