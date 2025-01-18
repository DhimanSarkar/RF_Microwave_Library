
// ###########################
// # TOOLBOX MICROWAVE
// ###########################
// V. 0.1 BETA
// Tibault Reveyrand
// 2007

// path=SCI+"/contrib/uW/help/";
// txt = help_skeleton("uW_MES_read",path);

// ###########################
// # Lecture de fichier MES
// ###########################


function dataset=uW_MES_read(filename)

dataset=tlist( ['MES_dataset','info','network'],[],list());
// network=tlist( ['MES_network','info','curve'],[],list());
// curve=tlist( ['MES_curve','info','plot'],list(),list());
// dataplot=tlist( ['MES_plot','v1','i1','v2','i2','S2P','Cgs','Cds','Gm','Gd','Cds','Ri','Tau','Rgd'],[],[],[],[],[],[],[],[],[],[],[],[],[]);





// Lecture d'un reseau MES


// path="F:\Korrigan\Modeles\QinetiQ\Iona\2x125\";
// fichier="2x125.mes";

// filename=path+fichier;

// Lecture des données

data=mgetl(filename);

// Dataset
dataset.info=data(1:5);

// Lecture des courbes

index=grep(data,"! Mesure:");
s=size(data);index=[index,s(1)+2];

// ### WAIT
win_wait=waitbar(0,"Read data from MES file");

for i=1:length(index)-1,

	// ### WAIT
	waitbar(i/(length(index)-1),win_wait); 

	
	
	// disp(i);
	// Lit les info du réseau
	info_reseau=data([index(i)+2,index(i)+3,index(i)+4,index(i)+5,index(i)+7]);
	
	// Trouve l'index du réseau
	nb_reseau=size(dataset.network);
	Reseau_existant=%F;
	
	// Teste l'existance du réseau
	if (nb_reseau~=0),
		for z=1:nb_reseau,
			if (dataset.network(z).info == info_reseau)  then,
				Reseau_existant=%T;
				index_network=z;
			end;
		end;
	end;
	
	
	// Si le réseau n'existe pas... on le rajoute
	
	if (Reseau_existant==%F) then,
		network=tlist( ['MES_network','info','curve'],[],list());
		network.info=info_reseau;
		dataset.network($+1)=network;
		index_network=size(dataset.network);
	end;
	
	
	// ##########################################################
	// # Creation de l'objet CURVE : Appel => curve.plot(i).v1
	// ##########################################################
	// ### Lecture des infos de la courbe
	curve=tlist( ['MES_curve','info','plot'],[],list());
	curve.info=data([index(i),index(i)+1,index(i)+6]);
	
	
	// #### Lecture des points courbe
	mes_data=data(index(i)+8:index(i+1)-2);s1=size(mes_data);s1=s1(1);
	
	for j=1:s1,
		dataplot=tlist( ['MES_plot','v1','i1','v2','i2','S2P','di1dv1','di1dv2','di2dv1','di2dv2','Cgs','Cgd','Gm','Gd','Cds','Ri','Tau','Rgd'],[],[],[],[],[],[],[],[],[],[],[],[],[]);
		
		temp_data=tokens(strsubst(mes_data(j),",",", "),",");
		s=size(temp_data);s=s(1);
		temp_VI=evstr("["+temp_data(1)+"]");
		dataplot.v1=temp_VI(1);
		dataplot.i1=temp_VI(2);
		dataplot.v2=temp_VI(3);
		dataplot.i2=temp_VI(4);

		if (s>=2) then,
			dataplot.S2P=strsubst(temp_data(2)," ","");
		end;
		
		// Debug
		// if dataplot.S2P=="AN7" then, disp(string(i)+" -- "+string(j)); end;
		//
		
		if (s==6) then,
		
			// Copie des dérivées
			temp_int=evstr("["+temp_data(3)+"]");
			dataplot.di1dv1=temp_int(1);
			dataplot.di1dv2=temp_int(2);

			temp_int=evstr("["+temp_data(4)+"]");
			dataplot.di2dv1=temp_int(1);
			dataplot.di2dv2=temp_int(2);			
			
		
			temp_int=evstr("["+temp_data(6)+"]");
			dataplot.Cgs=temp_int(1);
			dataplot.Cgd=temp_int(2);
			dataplot.Gm=temp_int(3);
			dataplot.Gd=temp_int(4);
			dataplot.Cds=temp_int(5);
			dataplot.Ri=temp_int(6);
			dataplot.Tau=temp_int(7);
			dataplot.Rgd=temp_int(8);			
		end;
		curve.plot($+1)=dataplot;
	end;
	
	// ### Rajout de la courbe dans le réseau
	dataset.network(index_network).curve($+1)=curve;

end;
// TK_barre_del();
winclose(win_wait);

endfunction;
